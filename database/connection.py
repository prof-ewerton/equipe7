"""import sqlite3

def get_connection():
    connection = sqlite3.connect('sistema.db')
    return connection.row_factory = sqlite3.Row
"""
import os
import sqlite3

def get_connection():
    
    pasta_local = os.path.dirname(os.path.abspath(__file__))
    caminho_banco = os.path.join(pasta_local, "sistema.db")
    conexao = sqlite3.connect(caminho_banco) 
    
    return conexao