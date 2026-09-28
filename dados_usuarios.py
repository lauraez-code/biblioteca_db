import sqlite3

conn = sqlite3.connect("biblioteca.db")

conn.execute("DROP TABLE IF EXISTS usuarios")

conn.execute("CREATE TABLE usuarios (nome TEXT NOT NULL, senha TEXT NOT NULL, email TEXT NOT NULL, PRIMARY KEY (email))")

conn.close()