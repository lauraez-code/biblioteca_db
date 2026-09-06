#**livros** (*id, id_autor, titulo, ano_publicacao, editora_id, disponivel*)

import sqlite3

conn = sqlite3.connect("biblioteca.db")

conn.execute("DROP TABLE IF EXISTS livros")

conn.execute('''CREATE TABLE livros (
id INTEGER PRIMARY KEY AUTOINCREMENT, 
id_autor INTEGER REFERENCES autores(id), 
titulo TEXT NOT NULL, 
ano_publicacao DATE NOT NULL, 
editora_id INTEGER REFERENCES editoras(id), 
disponivel INTEGER CHECK (disponivel IN (0,1)))''')

conn.executemany("INSERT INTO livros(id_autor, titulo, ano_publicacao, editora_id, disponivel) VALUES (?, ?, ?, ?, ?)", 
                 [(1, "Harry Potter", "05-02-2000", 1, 1,), (2, "Percy Jackson", "04-03-1998", 2, 0,)])

conn.commit()