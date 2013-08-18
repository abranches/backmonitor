from proto_classes.node_data_pb2 import NodeData

class Node(object):

    NODE_DATA_FIELDS = ("language",
                        "language_version",
                        "hostname",
                        "uname",
                        "exec_path",)

    def __init__(self, node_id):
        self.node_id = node_id

        self.ip_addr = None
        self.connected = False
        self.last_conn_time = None

        self._data = NodeData()

    def load_data(self, protobuf):
        self._data.ParseFromString(protobuf)

    def serialize_data(self):
        return self.data.SerializeToString()

    @property
    def language(self):
        return (self._data.language, self._data.language_version)

    @property
    def hostname(self):
        return self._data.hostname

    def get(self, key):
        if key not in self.NODE_DATA_FIELDS:
            raise KeyError("'%s' is not a valid node data field")
        return getattr(self._data, key)

    def set(self, key, value):
        if key not in self.NODE_DATA_FIELDS:
            raise KeyError("'%s' is not a valid node data field")
        setattr(self._data, key, value)
