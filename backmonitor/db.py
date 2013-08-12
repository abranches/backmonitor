import sqlite3
import threading

conn = sqlite3.connect("ola.db", check_same_thread=False)
c = conn.cursor()

def go():
    conn.execute("select 123")

threading.Thread(target=go).start()

c.execute("select 929823")
