from database.connection import get_connection
import sqlite3

def install():
    connection = get_connection()

    try:
        
        connection.execute("""CREATE TABLE IF NOT EXISTS pesquisadores (id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL DEFAULT 0,
        ativo BOOLEAN NOT NULL DEFAULT 0,
        especialidade TEXT NOT NULL)""")

        total = connection.execute("SELECT COUNT(*) FROM pesquisadores").fetchone()[0]
        if total == 0:
            connection.executemany("INSERT INTO pesquisadores (nome, idade, ativo, especialidade) VALUES (?, ?, ?, ?)",
              [("João", 38, True, "Arqueologia"),
               ("Maria", 25, True, "Arqueologia"),
               ("Mário", 72, False, "Paleontologia"),
               ("Pedro", 21, True, "Museologia"),
               ("José", 67, False, "Arqueologia"),
                ],)
        connection.commit()

    finally:
        connection.close()
    
    connection = get_connection()

    try:
        connection.execute("DROP TABLE IF EXISTS dinossauros;")
        
        connection.execute("""
            CREATE TABLE IF NOT EXISTS dinossauros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade TEXT NOT NULL,
                carnivoro BOOLEAN NOT NULL,
                especie TEXT NOT NULL
            )
        """)

        cursor = connection.execute("SELECT COUNT(*) FROM dinossauros")
        if cursor.fetchone()[0] == 0:
            connection.execute(
                "INSERT INTO dinossauros (nome, idade, carnivoro, especie ) VALUES (?, ?, ?, ?)",
                ("bob","12",True,"TiranossauroRex"),
                )
            connection.execute(
                "INSERT INTO dinossauros (nome, idade, carnivoro, especie ) VALUES (?, ?, ?, ?)",
                ("tony","13",False,"Mosassauro"),
                )
            connection.execute(
                "INSERT INTO dinossauros (nome, idade, carnivoro, especie ) VALUES (?, ?, ?, ?)",
                ("patatchi","17",True,"Pterodactilo"),
                )
            connection.execute(
                "INSERT INTO dinossauros (nome, idade, carnivoro, especie ) VALUES (?, ?, ?, ?)",
                ("Carna","16",False,"Mosassauro"),
                )
            connection.execute(
                "INSERT INTO dinossauros (nome, idade, carnivoro, especie ) VALUES (?, ?, ?, ?)",
                ("Poppy","9",False,"Estegossauro"),
                )
                

        connection.commit()
        
    finally:
        connection.close()
    
    connection = get_connection()

    
    try:
        connection.execute("DROP TABLE IF EXISTS habitat;")    
        
        connection.execute("""CREATE TABLE IF NOT EXISTS habitat (id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        capacidade INTEGER NOT NULL DEFAULT 0,
        seguro BOOLEAN NOT NULL DEFAULT 0,
        bioma TEXT NOT NULL)""")

        total_habitat = connection.execute("SELECT COUNT(*) FROM habitat").fetchone()[0]
        if total == 0:
            connection.executemany("INSERT INTO habitat (nome, capacidade, seguro, bioma) VALUES (?, ?, ?, ?)",
              [("Velociraptor", 12, True, "Pantanal"),
               ("Trex", 33, False, "Amazônia"),
               ("Megalodonte", 5, False, "Cerrado"),
               ("Animais marinhos minúsculos ", 8, True, "Caatinga"),
               ("Aves jurássicas", 14, True, "Pampas"),
                ],)
        connection.commit()

    finally:
        connection.close()

if __name__ == "__main__":
    install()
    print("Banco de dados instalado com sucesso.")
