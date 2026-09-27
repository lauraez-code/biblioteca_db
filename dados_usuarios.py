import sqlite3

conn = sqlite3.connect("biblioteca.db")

conn.execute("DROP TABLE usuarios")

conn.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT \
             , nome TEXT NOT NULL, senha TEXT NOT NULL)")

conn.close()