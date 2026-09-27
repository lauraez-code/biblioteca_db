import sqlite3

conn = sqlite3.connect("biblioteca.db")

conn.execute("DROP TABLE IF EXISTS emprestimos")

sql_create = """
    CREATE TABLE emprestimos (id INTEGER PRIMARY KEY AUTOINCREMENT,
        livro_id INTEGER REFERENCES livros(id),
        usuario_id INTEGER REFERENCES usuarios(id),
        data_emprestimo DATE DEFAULT CURRENT_DATE,
        data_devolucao DATE)
"""
conn.execute(sql_create)
