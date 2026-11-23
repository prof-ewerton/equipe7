from database.connection import get_connection

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


if __name__ == "__main__":
    install()
    print("Banco de dados instalado com sucesso.")

