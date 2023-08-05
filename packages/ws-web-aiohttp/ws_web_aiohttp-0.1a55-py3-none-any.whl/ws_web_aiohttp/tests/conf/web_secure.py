import os
import modconf
import ssl

from ws_web_aiohttp.tests.conf.log import *

url = 'www.charlesrymal.com'

certfile = '/etc/letsencrypt/live/www.charlesrymal.com/fullchain.pem'
keyfile = '/etc/letsencrypt/live/www.charlesrymal.com/privkey.pem'

google_oauth2 = modconf.import_conf('google_oauth2', os.path.join(os.environ['HOME'], 'config'))

PG = modconf.import_conf('web_sheets_postgresql', os.path.join(os.environ['HOME'], 'config'))

ws_sheets_server = modconf.import_conf('ws_sheets_server.tests.conf.simple')


SSL_CONTEXT = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
SSL_CONTEXT.load_cert_chain(certfile, keyfile)


class Conf(object):
    SCHEME = 'https'
    SCHEME_WS = 'wss'
    PORT = 8443

    @classmethod
    def url_root(cls):
        return '{}://localhost:{}'.format(cls.SCHEME, cls.PORT)

    @classmethod
    def ws_root(cls):
        return '{}://localhost:{}'.format(cls.SCHEME_WS, cls.PORT)


