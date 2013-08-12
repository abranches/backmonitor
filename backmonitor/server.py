import logging
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor

from protocol import BackmonitorTwistedFactory

log = logging.getLogger(__name__)

LISTEN_PORT = 8990

class BackmonitorServer(object):
    def __init__(self):
        pass

    def start(self):
        log.debug("Starting backmonitor server")
        endpoint = TCP4ServerEndpoint(reactor, LISTEN_PORT)
        endpoint.listen(BackmonitorTwistedFactory(self))
        reactor.run()

    def stop(self):
        log.debug("Stopping server")
        rector.stop()

    def on_new_message(self, message):
        log.debug("Got new message: %s" % message)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    server = BackmonitorServer()
    server.start()
