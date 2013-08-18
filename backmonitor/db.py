import sqlite3
import threading

from node import Node

class Database(object):
    def __init__(self):
        self.conn = None

    def connect(self):
        raise NotImplementedError()

    def close(self):
        if self.conn is not None:
            self.conn.close()

    def insert_node(self, node):
        c = self.conn.cursor()
        c.execute("INSERT INTO nodes (str_id, host_ip, connected,\
                                     last_conn_time, node_data)\
                   VALUES (%s, %s, %s, %s, %s)",
                   (node.node_id, node.ip_addr, host.connected,
                    node.last_conn_time, node.serialize_data()))
        self.conn.commit()

    def get_node(self, node_id):
        c = self.conn.cursor()
        c.execute("SELECT str_id, host_ip, connected,\
                          last_conn_time, node_data\
                   FROM nodes\
                   WHERE str_id=%s", (node_id,))
        row = c.fetchone()
        if not row:
            return None

        str_id, host_ip, connected, last_conn_time, node_data = row[0]
        node = Node(str_id)
        node.ip_addr = host_ip
        node.connected = connected
        node.last_conn_time = last_conn_time
        if node_data:
            node.load_data(node_data)

        return node

    def _get_node_id(self, node):
        c = self.conn.cursor()
        c.execute("SELECT id FROM events WHERE str_id=%s", (node.node_id,))
        return c.fetchone() is not None

    def insert_event(self, event, node):
        c = self.conn.cursor()
        c.execute("INSERT INTO events (node, timestamp, type, \
                                       name, event_protobuf)
                   VALUES (%s, %s, %s, %s, 5s)",
                   (self._get_node_id(node), event.timestamp, event.type,
                    event.name, event.serialize()))
        self.conn.commit()


class SQLiteDB(Database):
    def __init__(self, db_file):
        super(self, SQLiteDB).__init__()
        self.db_file = db_file

    def _create_if_not_exists(self):
        with open("db_schema.sql") as f:
            schema = f.read()
        self.conn.cursor().execute(schema)
        self.conn.commit()

    def connect(self):
        self.conn = sqlite3.connect(self.db_file)
        self._create_if_not_exists(self)
