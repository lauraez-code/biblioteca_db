#**livros** (*id, id_autor, titulo, ano_publicacao, editora_id, disponivel*)

import sqlite3

conn = sqlite3.connect("biblioteca.db")

conn.execute("DROP TABLE IF EXISTS livros")

conn.execute("CREATE TABLE livros (id INTEGER PRIMARY KEY AUTOINCREMENT, id_autor INTEGER REFERENCES autores(id), titulo TEXT NOT NULL, ano_publicacao DATE NOT NULL, editora_id INTEGER REFERENCES editoras(id), disponivel IN(0,1)")

conn.executemany("INSERT INTO (data, id_usuario) VALUES (?, ?)", 
                 [('03-02-2026', 1), ("04-06-2026", 2,)])

conn.commit()