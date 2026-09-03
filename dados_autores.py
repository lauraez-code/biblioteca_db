import sqlite3

conn = sqlite3.connect("biblioteca.db")

conn.execute("DROP TABLE IF EXISTS autores")

conn.execute("CREATE TABLE autores (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL)")

conn.executemany("INSERT INTO autores(nome) VALUES (?)", 
                 [("Joana",), ("Arthur",)])

conn.commit()