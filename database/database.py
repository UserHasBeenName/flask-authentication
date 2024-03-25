from flask import g
from sqlite3 import connect
from random import choice
ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def open_db():
    if getattr(g, "_database", None) is None:
        g._db = connect("database/users.db")
    return g._db
def new_salt():
    return ''.join(choice(ALPHABET) for i in range(16))
def new_uid():
    return 'uid_'+''.join(choice(ALPHABET) for i in range(7))