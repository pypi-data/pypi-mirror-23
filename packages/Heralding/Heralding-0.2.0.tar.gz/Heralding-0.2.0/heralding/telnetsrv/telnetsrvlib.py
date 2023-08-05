# license: LGPL
# Thanks a lot to the author of original telnetsrvlib - Ian Epperson (https://github.com/ianepperson)!

import socket
import curses
import logging
import socketserver
import curses.ascii
import curses.has_key


log = logging.getLogger(__name__)

BELL = bytes([7])
ANSI_START_SEQ = b'['
ANSI_KEY_TO_CURSES = {
    b'A': curses.KEY_UP,
    b'B': curses.KEY_DOWN,
    b'C': curses.KEY_RIGHT,
    b'D': curses.KEY_LEFT,
}

# Telnet protocol characters (don't change)
IAC = bytes([255])  # "Interpret As Command"
DONT = bytes([254])
DO = bytes([253])
WONT = bytes([252])
WILL = bytes([251])
theNULL = bytes([0])

SE = bytes([240])  # Subnegotiation End
NOP = bytes([241])  # No Operation
SB = bytes([250])  # Subnegotiation Begin

# Telnet protocol options code (don't change)
# These ones all come from arpa/telnet.h
ECHO = bytes([1])  # echo
SGA = bytes([3])  # suppress go ahead
TTYPE = bytes([24])  # terminal type
NAWS = bytes([31])  # window size
LINEMODE = bytes([34])  # Linemode option
NEW_ENVIRON = bytes([39])  # New - Environment variables
NOOPT = bytes([0])

IS = bytes([0])
SEND = bytes([1])


class TelnetHandlerBase(socketserver.BaseRequestHandler):
    """A telnet server based on the client in telnetlib"""

    # Several methods are not fully defined in this class, and are
    # very specific to either a threaded or green implementation.
    # These methods are noted as #abstracmethods to ensure they are
    # properly made concrete.
    # (abc doesn't like the BaseRequestHandler - sigh)
    # __metaclass__ = ABCMeta

    # What I am prepared to do?
    DOACK = {
        ECHO: WILL,
        SGA: WILL,
        NEW_ENVIRON: WONT,
    }
    # What do I want the client to do?
    WILLACK = {
        ECHO: DONT,
        SGA: DO,
        NAWS: DONT,
        TTYPE: DO,
        LINEMODE: DONT,
        NEW_ENVIRON: DO,
    }
    # Default terminal type - used if client doesn't tell us its termtype
    TERM = "ansi"
    # Keycode to name mapping - used to decide which keys to query
    KEYS = {  # Key escape sequences
        curses.KEY_UP: 'Up',  # Cursor up
        curses.KEY_DOWN: 'Down',  # Cursor down
        curses.KEY_LEFT: 'Left',  # Cursor left
        curses.KEY_RIGHT: 'Right',  # Cursor right
        curses.KEY_DC: 'Delete',  # Delete right
        curses.KEY_BACKSPACE: 'Backspace',  # Delete left
    }
    # Reverse mapping of KEYS - used for cooking key codes
    ESCSEQ = {
    }
    # Terminal output escape sequences
    CODES = {
        'DEOL': b'',  # Delete to end of line
        'DEL': b'',  # Delete and close up
        'INS': b'',  # Insert space
        'CSRLEFT': b'',  # Move cursor left 1 space
        'CSRRIGHT': b'',  # Move cursor right 1 space
    }

    # --------------------------- Environment Setup ----------------------------

    def __init__(self, request, client_address, server):
        """Constructor.

        When called without arguments, create an unconnected instance.
        With a hostname argument, it connects the instance; a port
        number is optional.
        """
        # Am I doing the echoing?
        self.DOECHO = True
        # What opts have I sent DO/DONT for and what did I send?
        self.DOOPTS = {}
        # What opts have I sent WILL/WONT for and what did I send?
        self.WILLOPTS = {}

        # What commands does this CLI support
        self.sock = None  # TCP socket
        self.rawq = b''  # Raw input string
        self.sbdataq = b''  # Sub-Neg string
        self.eof = 0  # Has EOF been reached?
        self.iacseq = b''  # Buffer for IAC sequence.
        self.sb = 0  # Flag for SB and SE sequence.
        self.history = []  # Command history

        socketserver.BaseRequestHandler.__init__(self, request, client_address, server)

    class false_request:
        def __init__(self):
            self.sock = None

    def setterm(self, term):
        """Set the curses structures for this terminal"""
        raise NotImplementedError("Please Implement the setterm method")

    def setup(self):
        """Connect incoming connection to a telnet session"""
        try:
            self.TERM = self.request.term
        except:
            pass
        self.setterm(self.TERM)
        self.sock = self.request._sock
        for k in self.DOACK.keys():
            self.sendcommand(self.DOACK[k], k)
        for k in self.WILLACK.keys():
            self.sendcommand(self.WILLACK[k], k)

    def finish(self):
        """End this session"""
        log.debug("Session disconnected.")
        try:
            self.sock.shutdown(socket.SHUT_RDWR)
        except:
            pass
        self.session_end()

    def session_start(self):
        pass

    def session_end(self):
        pass

    # ------------------------- Telnet Options Engine --------------------------

    def sendcommand(self, cmd, opt=None):
        "Send a telnet command (IAC)"
        if cmd in [DO, DONT]:
            if opt not in self.DOOPTS:
                self.DOOPTS[opt] = None
            if (((cmd == DO) and (self.DOOPTS[opt] is not True))
                    or ((cmd == DONT) and (self.DOOPTS[opt] is not False))):
                self.DOOPTS[opt] = (cmd == DO)
                self.writecooked(IAC + cmd + opt)
        elif cmd in [WILL, WONT]:
            if opt not in self.WILLOPTS:
                self.WILLOPTS[opt] = b''
            if (((cmd == WILL) and (self.WILLOPTS[opt] is not True))
                    or ((cmd == WONT) and (self.WILLOPTS[opt] is not False))):
                self.WILLOPTS[opt] = (cmd == WILL)
                self.writecooked(IAC + cmd + opt)
        else:
            self.writecooked(IAC + cmd)

    # ---------------------------- Input Functions -----------------------------

    def _readline_do_echo(self, echo):
        """Determine if we should echo or not"""
        return echo is True or (echo is None and self.DOECHO is True)

    def _readline_echo(self, char, echo):
        """Echo a recieved character, move cursor etc..."""
        if self._readline_do_echo(echo):
            self.write(char)

    _current_line = b''
    _current_prompt = b''

    def ansi_to_curses(self, char):
        """Handles reading ANSI escape sequences"""
        # ANSI sequences are:
        # ESC [ <key>
        # If we see ESC, read a char
        if char != 27:     # ESC = bytes([27])
            return char
        # If we see [, read another char
        if convert_to_bytes(self.getc(block=True)) != ANSI_START_SEQ:
            self._readline_echo(BELL, True)
            return 0   # theNull = bytes([0])
        key = convert_to_bytes(self.getc(block=True))
        # Translate the key to curses
        try:
            return ANSI_KEY_TO_CURSES[key]
        except:
            self._readline_echo(BELL, True)
            return 0

    def _readline_insert(self, charb, echo, insptr, line):
        """Deal properly with inserted chars in a line."""
        if not self._readline_do_echo(echo):
            return
        # Write out the remainder of the line
        self.write(charb + b''.join(line[insptr:]))
        # Cursor Left to the current insert point
        char_count = len(line) - insptr
        self.write(self.CODES['CSRLEFT'] * char_count)

    def readline(self, echo=None, prompt=b'', use_history=True):
        """Return a line of bytes, including the terminating LF
           If echo is true always echo, if echo is false never echo
           If echo is None follow the negotiated setting.
           prompt is the current prompt to write (and rewrite if needed)
           use_history controls if this current line uses (and adds to) the command history.
        """

        line = []
        insptr = 0
        histptr = len(self.history)

        if self.DOECHO:
            self.write(prompt)
            self._current_prompt = prompt
        else:
            self._current_prompt = b''

        self._current_line = b''

        while True:
            c = self.getc(block=True)
            c = self.ansi_to_curses(c)
            cb = convert_to_bytes(c)

            if cb == theNULL:
                continue

            elif c == curses.KEY_LEFT:
                if insptr > 0:
                    insptr = insptr - 1
                    self._readline_echo(self.CODES['CSRLEFT'], echo)
                else:
                    self._readline_echo(BELL, echo)
                continue
            elif c == curses.KEY_RIGHT:
                if insptr < len(line):
                    insptr = insptr + 1
                    self._readline_echo(self.CODES['CSRRIGHT'], echo)
                else:
                    self._readline_echo(BELL, echo)
                continue
            elif c == curses.KEY_UP or c == curses.KEY_DOWN:
                if not use_history:
                    self._readline_echo(BELL, echo)
                    continue
                if c == curses.KEY_UP:
                    if histptr > 0:
                        histptr = histptr - 1
                    else:
                        self._readline_echo(BELL, echo)
                        continue
                elif c == curses.KEY_DOWN:
                    if histptr < len(self.history):
                        histptr = histptr + 1
                    else:
                        self._readline_echo(BELL, echo)
                        continue
                line = []
                if histptr < len(self.history):
                    line.extend(self.history[histptr])
                for char in range(insptr):
                    self._readline_echo(self.CODES['CSRLEFT'], echo)
                self._readline_echo(self.CODES['DEOL'], echo)
                self._readline_echo(b''.join(line), echo)
                insptr = len(line)
                continue
            elif cb == bytes([3]):
                self._readline_echo(b'\n' + convert_to_bytes(curses.ascii.unctrl(c)) + b' ABORT\n', echo)
                return b''
            elif cb == bytes([4]):
                if len(line) > 0:
                    self._readline_echo(b'\n' + convert_to_bytes(curses.ascii.unctrl(c)) + b' ABORT (QUIT)\n', echo)
                    return b''
                self._readline_echo(b'\n' + convert_to_bytes(curses.ascii.unctrl(c)) + b' QUIT\n', echo)
                return b'QUIT'
            elif cb == bytes([10]):
                self._readline_echo(cb, echo)
                result = b''.join(convert_to_bytes(elem) for elem in line)
                if use_history:
                    self.history.append(result)
                if echo is False:
                    if prompt:
                        self.write(bytes([10]))
                    log.debug('readline: %s(hidden text)', prompt)
                else:
                    log.debug('readline: %s%r', prompt, result)
                return result
            elif c == curses.KEY_BACKSPACE or cb == bytes([127]) or cb == bytes([8]):
                if insptr > 0:
                    self._readline_echo(self.CODES['CSRLEFT'] + self.CODES['DEL'], echo)
                    insptr = insptr - 1
                    del line[insptr]
                else:
                    self._readline_echo(BELL, echo)
                continue
            elif c == curses.KEY_DC:
                if insptr < len(line):
                    self._readline_echo(self.CODES['DEL'], echo)
                    del line[insptr]
                else:
                    self._readline_echo(BELL, echo)
                continue
            else:
                if c < 32:
                    c = curses.ascii.unctrl(c)
                    cb = convert_to_bytes(c)
                if len(line) > insptr:
                    self._readline_insert(cb, echo, insptr, line)
                else:
                    self._readline_echo(cb, echo)
            line[insptr:insptr] = cb
            insptr = insptr + len(cb)
            if self._readline_do_echo(echo):
                self._current_line = line

    # abstractmethod
    def getc(self, block=True):
        """Return one character from the input queue"""
        # This is very different between green threads and real threads.
        raise NotImplementedError("Please Implement the getc method")

    # --------------------------- Output Functions -----------------------------

    def write(self, data_bytes):
        """Send a packet to the socket. This function cooks output."""
        data_bytes = data_bytes.replace(IAC, IAC + IAC)
        data_bytes = data_bytes.replace(bytes([10]), bytes([13]) + bytes([10]))
        self.writecooked(data_bytes)

    def writecooked(self, data_bytes):
        """Put data directly into the output queue (bypass output cooker)"""
        self.sock.sendall(data_bytes)

    def writeline(self, data_bytes):
        """Send a packet with line ending."""
        log.debug('writing line %r' % data_bytes)
        self.write(data_bytes + bytes([10]))

    # ------------------------------- Input Cooker -----------------------------
    def _inputcooker_getc(self, block=True):
        """Get one character from the raw queue. Optionally blocking.
        Raise EOFError on end of stream. SHOULD ONLY BE CALLED FROM THE
        INPUT COOKER."""
        if self.rawq:
            ret = self.rawq[0]
            self.rawq = self.rawq[1:]
            return bytes([ret]) if ret else b''
        if not block:
            if not self.inputcooker_socket_ready():
                return b''
        ret = self.sock.recv(20)
        self.eof = not (ret)
        # if isinstance(ret, bytes):
        #   ret = bytes([ret])
        self.rawq = self.rawq + ret
        if self.eof:
            raise EOFError
        return self._inputcooker_getc(block)

    # abstractmethod
    def inputcooker_socket_ready(self):
        """Indicate that the socket is ready to be read"""
        # Either use a green select or a real select
        # return select([self.sock.fileno()], [], [], 0) != ([], [], [])
        raise NotImplementedError("Please Implement the inputcooker_socket_ready method")

    def _inputcooker_ungetc(self, char):
        """Put characters back onto the head of the rawq. SHOULD ONLY
        BE CALLED FROM THE INPUT COOKER."""
        self.rawq = char + self.rawq

    def _inputcooker_store(self, char):
        """Put the cooked data in the correct queue"""
        if self.sb:
            self.sbdataq = self.sbdataq + char
        else:
            self.inputcooker_store_queue(char)

    # abstractmethod
    def inputcooker_store_queue(self, char):
        """Put the cooked data in the output queue (possible locking needed)"""
        raise NotImplementedError("Please Implement the inputcooker_store_queue method")

    def inputcooker(self):
        """Input Cooker - Transfer from raw queue to cooked queue.

        Set self.eof when connection is closed.  Don't block unless in
        the midst of an IAC sequence.
        """
        try:
            while True:
                cb = self._inputcooker_getc()
                if not self.iacseq:
                    if cb == IAC:
                        self.iacseq += cb
                        continue
                    elif cb == bytes([13]) and not (self.sb):
                        c2b = self._inputcooker_getc(block=False)
                        if c2b == theNULL or c2b == b'':
                            cb = bytes([10])
                        elif c2b == bytes([10]):
                            cb = c2b
                        else:
                            self._inputcooker_ungetc(c2b)
                            cb = bytes([10])
                    elif cb in [x[0] for x in self.ESCSEQ.keys()]:
                        # Looks like the begining of a key sequence
                        codes = cb
                        for keyseq in self.ESCSEQ.keys():
                            if len(keyseq) == 0:
                                continue
                            while codes == keyseq[:len(codes)] and len(codes) <= keyseq:
                                if codes == keyseq:
                                    cb = self.ESCSEQ[keyseq]
                                    break
                                codes = codes + self._inputcooker_getc()
                            if codes == keyseq:
                                break
                            self._inputcooker_ungetc(codes[1:])
                            codes = codes[0]
                    self._inputcooker_store(cb)
                elif len(self.iacseq) == 1:
                    # IAC: IAC CMD [OPTION only for WILL/WONT/DO/DONT]
                    if cb in (DO, DONT, WILL, WONT):
                        self.iacseq += cb
                        continue
                    self.iacseq = b''
                    if cb == IAC:
                        self._inputcooker_store(cb)
                    else:
                        if cb == SB:  # SB ... SE start.
                            self.sb = 1
                            self.sbdataq = b''
                        elif cb == SE:  # SB ... SE end.
                            self.sb = 0
                        # Callback is supposed to look into
                        # the sbdataq
                elif len(self.iacseq) == 2:
                    self.iacseq = b''
        except (EOFError, socket.error):
            pass

    def authentication_ok(self):
        """Checks the authentication and sets the username of the currently connected terminal.  Returns True or False"""
        raise NotImplementedError("Please Implement the authentication_ok method")

    # ----------------------- Command Line Processor Engine --------------------

    def handle(self):
        """The actual service to which the user has connected."""
        self.authentication_ok()


def convert_to_bytes(c):
    if isinstance(c, int):
        if c < 256:
            cb = bytes([c])
        else:
            cb = None
    elif isinstance(c, str):
        cb = bytes(c, 'utf-8')
    else:
        cb = c
    return cb
# vim: set syntax=python ai showmatch:
