import sqlite3

conn = sqlite3.connect("biblioteca.db")

conn.execute("DROP TABLE IF EXISTS emprestimos")

sql_create = """
    CREATE TABLE emprestimos (id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER REFERENCES usuarios(id),
        data DATE DEFAULT CURRENT_DATE)
"""
conn.execute(sql_create)
