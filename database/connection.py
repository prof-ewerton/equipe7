import sqlite3

def get_connection():
    connection = sqlite3.connect('sistema.db')
    return connection.row_factory = sqlite3.Row

