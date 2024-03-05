from flask import g
from sqlite3 import connect
def open_db():
    if getattr(g, "_database", None) is None:
        g._db = connect("database/users.db")
    return g._db