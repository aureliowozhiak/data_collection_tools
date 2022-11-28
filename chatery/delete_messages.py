DB_STRING = 'chat_data.db'
import sqlite3

with sqlite3.connect(DB_STRING) as dbc:
    dbc.execute("DELETE FROM messages")