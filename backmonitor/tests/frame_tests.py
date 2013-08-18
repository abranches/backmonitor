import unittest
import random

from ..frame import Frame, decode_frame
from ..message import MessageType
from ..utilslib.strings import random_bytes

class FrameTestCase(unittest.TestCase):
    MSG_TYPE = MessageType.HELLO
    PAYLOAD = "Hello World!"

    def frame_setup(self, msg_type, payload):
        self.msg_type = msg_type
        self.payload = payload
        self.frame = Frame(self.msg_type, self.payload)

    def setUp(self):
        self.frame_setup(self.MSG_TYPE, self.PAYLOAD)

    def tearDown(self):
        self.msg_type = None
        self.payload = None
        self.frame = None

    def test_eq_at_decode_after_encode(self):
        consumed_bytes, decoded = decode_frame(self.frame.encode())
        self.assertIsNotNone(self, decoded)
        self.assertEqual(self.frame, decoded,
                    "!!! decode(encode(X)) != X !!!")

    def test_raw_eq_at_decode_after_encode(self):
        consumed_bytes, decoded = decode_frame(self.frame.encode())
        self.assertIsNotNone(self, decoded)
        self.assertEqual(decoded.msg_type, self.msg_type)
        self.assertEqual(decoded.payload, self.payload)

    def test_encoded_size_matches_expected_calcsize(self):
        self.assertEqual(len(self.frame.encode()), self.frame.calcsize())


class RandomFrameTestCase(FrameTestCase):
    MIN_PAYLOAD_SIZE = 1
    MAX_PAYLOAD_SIZE = 512

    def setUp(self):
        msg_type = random.choice(MessageType.values())
        payload_size = random.randrange(self.MIN_PAYLOAD_SIZE,
                                        self.MAX_PAYLOAD_SIZE+1)
        payload = random_bytes(payload_size)
        self.frame_setup(msg_type, payload)

class EmptyPayloadFrameTestCase(RandomFrameTestCase):
    def setUp(self):
        self.frame_setup(random.choice(MessageType.values()), b"")
