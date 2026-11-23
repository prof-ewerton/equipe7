import sqlite3

def get_db_connection():
    connection = sqlite3.connect('')
    return connection.row_factory = sqlite3.Row