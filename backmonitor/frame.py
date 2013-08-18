import logging
import struct

from message import MessageType
from exceptions import FrameException

log = logging.getLogger(__name__)

FRAME_HEADER_STRUCT = ">BH"
FRAME_HEADER_SIZE = struct.calcsize(FRAME_HEADER_STRUCT)
FRAME_END = "\xFE"
FRAME_END_SIZE = len(FRAME_END)

class Frame(object):

    def __init__(self, msg_type, payload):
        self.msg_type = msg_type
        self.payload = payload

    def __str__(self):
        return "Frame(%s, len(payload)=%d)" % \
                (MessageType.key_of(self.msg_type), len(self.payload))

    def calcsize(self):
        return FRAME_HEADER_SIZE + len(self.payload) + FRAME_END_SIZE

    def encode(self):
        return struct.pack(FRAME_HEADER_STRUCT,
                           self.msg_type,
                           len(self.payload)) + self.payload + FRAME_END

    def __eq__(self, o):
        return self.msg_type == o.msg_type and self.payload == o.payload


def decode_frame(raw_data):
    """
    Try to create a frame instance from the raw data.
    It's assumed that raw_data is a buffer and can still be incomplete to
    create a valid frame or it has multiple frames packed into it.

    Arguments:
        raw_data - byte() with the raw data of the buffer

    Returns (bytes consumed, frame instance) or 
            (0, None) if no complete frame is in the buffer

    Raises FrameException if an invalid frame was detected.
    """
    log.debug("RAW DATA: %r" % raw_data)
    try:
        msg_type, payload_size = struct.unpack(FRAME_HEADER_STRUCT,
                                               raw_data[:FRAME_HEADER_SIZE])
    except struct.error:
        log.debug("Invalid frame - couldn't unpack headers")
        return 0, None

    frame_end = FRAME_HEADER_SIZE + payload_size + FRAME_END_SIZE
    if len(raw_data) < frame_end:
        log.debug("Invalid frame - incomplete frame (%d, %d)" % \
                    (len(raw_data), frame_end))
        return 0, None

    if raw_data[frame_end - FRAME_END_SIZE] != FRAME_END:
        raise FrameException(
                "Frame doesn't end with the expected FRAME_END marker")

    payload = raw_data[FRAME_HEADER_SIZE:frame_end-FRAME_END_SIZE]
    log.debug("PAYLOAD: %r" % payload)

    if msg_type not in MessageType.values():
        raise FrameException("Frame has invalid message type")

    return frame_end, Frame(msg_type, payload)



