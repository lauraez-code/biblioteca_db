import sqlite3

conn = sqlite3.connect("biblioteca.db")

conn.execute("DROP TABLE IF EXISTS livros")

sql_create = """CREATE TABLE livros (id INTEGER PRIMARY KEY AUTOINCREMENT, 
            titulo TEXT NOT NULL, autor_id INTEGER REFERENCES autores(id), 
            editora_id INTEGER REFERENCES editoras(id),
            ano_publicacao INTEGER,
            edicao INTEGER,
            estoque INTEGER,
            )"""

conn.execute(sql_create)

