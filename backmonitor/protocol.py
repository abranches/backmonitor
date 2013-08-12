import logging
from twisted.internet.protocol import Factory, Protocol

from frame import decode_frame
from message import decode_message

log = logging.getLogger(__name__)

class ConnectionManager(object):

    def __init__(self, backmonitor, addr):
        self.backmonitor = backmonitor
        self.addr = addr
        self._buffer = bytes()

        self._open = False
        self.bytes_received = 0
        self.frames_received = 0

    @property
    def open(self):
        return self._open

    def _on_data_received(self, data):
        log.debug("_on_data_received(), data length=%d" % len(data))
        self._buffer += data

        while self._buffer:
            consumed_bytes, frame = decode_frame(self._buffer)
            if consumed_bytes == 0:
                return

            self.bytes_received += consumed_bytes
            self._buffer = self._buffer[consumed_bytes:]
            self._process_frame(frame)

    def _process_frame(self, frame):
        log.debug("Processing new frame")
        message = decode_message(frame)
        self.backmonitor.on_new_message(message)
        self.frames_received += 1


class BackmonitorTwistedProtocol(Protocol):

    def __init__(self, factory, conn_manager):
        self.factory = factory
        self.conn_manager = conn_manager

    def connectionMade(self):
        log.debug("New connection estabilished")
        self.conn_manager._open = True
        self.factory.connected_peers += 1

    def dataReceived(self, data):
        self.conn_manager._on_data_received(data)


class BackmonitorTwistedFactory(Factory):

    def __init__(self, backmonitor):
        self.connected_peers = 0
        self.backmonitor = backmonitor

    def buildProtocol(self, addr):
        return BackmonitorTwistedProtocol(self, ConnectionManager(self.backmonitor, addr))
