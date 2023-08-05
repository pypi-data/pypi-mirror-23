# Copyright (C) 2017 Johnny Vestergaard <jkv@unixcluster.dk>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import ssl
import sys
import logging

import gevent
import gevent.event
from gevent import Greenlet
from gevent.server import StreamServer

import heralding.capabilities.handlerbase
from heralding.reporting.file_logger import FileLogger
from heralding.reporting.syslog_logger import SyslogLogger
from heralding.misc.common import on_unhandled_greenlet_exception, generate_self_signed_cert

from ipify import get_ip

logger = logging.getLogger(__name__)


class SSLStreamServer(StreamServer):
    """StreamServer class, but with handling of 'NO_SHARED_CIPHER' error."""

    def wrap_socket_and_handle(self, client_socket, address):
        try:
            return super().wrap_socket_and_handle(client_socket, address)
        except ssl.SSLError as err:
            if err.reason == "NO_SHARED_CIPHER":
                target_port = self.server_port
                client_address = "{0}:{1}".format(*address)
                error_message = "{0} tried to connect {1} port, " \
                                "but no supported ciphers were found!".format(client_address, target_port)
                logger.error(error_message)
            else:
                raise ssl.SSLError(err)


class Honeypot:
    public_ip = ''

    def __init__(self, config):
        """
        :param config: configuration dictionary.
        """
        assert config is not None
        self.readyForDroppingPrivs = gevent.event.Event()
        self.config = config
        self._servers = []
        self._greenlets = []

    def _record_and_lookup_public_ip(self):
        while True:
            try:
                Honeypot.public_ip = get_ip()
                logger.warning('Found public ip: {0}'.format(Honeypot.public_ip))
            except Exception as ex:
                Honeypot.public_ip = ''
                logger.warning('Could not request public ip from ipify, error: {0}'.format(ex))
            gevent.sleep(3600)

    def start(self):
        """ Starts services. """

        if 'public_ip_as_destination_ip' in self.config and self.config['public_ip_as_destination_ip'] is True:
            self._greenlets.append(gevent.spawn(self._record_and_lookup_public_ip))

        # start activity logging
        if 'activity_logging' in self.config:
            if 'file' in self.config['activity_logging'] and self.config['activity_logging']['file']['enabled']:
                logFile = self.config['activity_logging']['file']['filename']
                greenlet = FileLogger(logFile)
                greenlet.link_exception(on_unhandled_greenlet_exception)
                greenlet.start()
            if 'syslog' in self.config['activity_logging'] and self.config['activity_logging']['syslog']['enabled']:
                greenlet = SyslogLogger()
                greenlet.link_exception(on_unhandled_greenlet_exception)
                greenlet.start()

        for c in heralding.capabilities.handlerbase.HandlerBase.__subclasses__():

            cap_name = c.__name__.lower()
            if cap_name in self.config['capabilities']:
                if not self.config['capabilities'][cap_name]['enabled']:
                    continue
                port = self.config['capabilities'][cap_name]['port']
                # carve out the options for this specific service
                options = self.config['capabilities'][cap_name]
                # capabilities are only allowed to append to the session list
                cap = c(options)

                try:
                    # Convention: All capability names which end in 's' will be wrapped in ssl.
                    if cap_name.endswith('s'):
                        pem_file = '{0}.pem'.format(cap_name)
                        self.create_cert_if_not_exists(cap_name, pem_file)
                        server = SSLStreamServer(('0.0.0.0', port), cap.handle_session,
                                                  keyfile=pem_file, certfile=pem_file)
                    else:
                        server = StreamServer(('0.0.0.0', port), cap.handle_session)

                    logger.debug('Adding {0} capability with options: {1}'.format(cap_name, options))
                    self._servers.append(server)
                    server_greenlet = Greenlet(server.start())
                    self._greenlets.append(server_greenlet)
                except Exception as ex:
                    error_message = "Could not start {0} server on port {1}. Error: {2}".format(c.__name__, port, ex)
                    logger.error(error_message)
                    sys.exit(error_message)
                else:
                    logger.info('Started {0} capability listening on port {1}'.format(c.__name__, port))

        self.readyForDroppingPrivs.set()
        gevent.joinall(self._greenlets)

    def stop(self):
        """Stops services"""

        for s in self._servers:
            s.stop()

        for g in self._greenlets:
            g.kill()

        logger.info('All workers stopped.')

    def blokUntilReadyForDroppingPrivs(self):
        self.readyForDroppingPrivs.wait()

    def create_cert_if_not_exists(self, cap_name, pem_file):
        if not os.path.isfile(pem_file):
            logger.debug('Generating certificate and key: {0}'.format(pem_file))

            cert_dict = self.config['capabilities'][cap_name]['protocol_specific_data']['cert']
            cert_cn = cert_dict['common_name']
            cert_country = cert_dict['country']
            cert_state = cert_dict['state']
            cert_locality = cert_dict['locality']
            cert_org = cert_dict['organization']
            cert_org_unit = cert_dict['organizational_unit']
            valid_days = int(cert_dict['valid_days'])
            serial_number = int(cert_dict['serial_number'])

            cert, key = generate_self_signed_cert(cert_country, cert_state, cert_org, cert_locality, cert_org_unit,
                                                  cert_cn, valid_days, serial_number)
            with open(pem_file, 'wb') as _pem_file:
                _pem_file.write(cert)
                _pem_file.write(key)
