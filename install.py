import sqlite3

def install():
    try:
        conexao = sqlite3.connect("sistema.db")
        
        cursor = conexao.cursor()
        
        print("Conexão realizada com sucesso.")
        
        except sqlite3.Error as erro:
            print("Erro ao conectar ao banco:", erro)

    try:
        cursor.execute("DROP TABLE IF EXISTS dinossauros;")
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS dinossauros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade TEXT NOT NULL,
                carnivoro INTEGER NOT NULL,
                especie TEXT NOT NULL
            )
        """)

        cursor = connection.execute("SELECT COUNT(*) FROM dinossauros")
        if cursor.fetchone()[0] == 0:
            cursor.execute(
                "INSERT INTO dinossauros (nome, idade, carnivoro, especie ) VALUES (?, ?, ?, ?)",
                ("bob","12",1,"TiranossauroRex"),
                )
            cursor.execute(
                "INSERT INTO dinossauros (nome, idade, carnivoro, especie ) VALUES (?, ?, ?, ?)",
                ("tony","13",0,"Mosassauro"),
                )
            cursor.execute(
                "INSERT INTO dinossauros (nome, idade, carnivoro, especie ) VALUES (?, ?, ?, ?)",
                ("patatchi","17",1,"Pterodactilo"),
                )
            cursor.execute(
                "INSERT INTO dinossauros (nome, idade, carnivoro, especie ) VALUES (?, ?, ?, ?)",
                ("Carna","16",0,"Mosassauro"),
                )
            cursor.execute(
                "INSERT INTO dinossauros (nome, idade, carnivoro, especie ) VALUES (?, ?, ?, ?)",
                ("Poppy","9",0,"Estegossauro"),
                )
                

        conexao.commit()

    finally:
        conexao.close()