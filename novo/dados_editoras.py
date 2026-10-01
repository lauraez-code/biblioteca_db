import sqlite3

conn = sqlite3.connect("biblioteca.db")

conn.execute("DROP TABLE IF EXISTS editoras")

conn.execute("CREATE TABLE editoras (id INTEGER PRIMARY KEY AUTOINCREMENT \
             , nome TEXT NOT NULL)")

conn.close()
