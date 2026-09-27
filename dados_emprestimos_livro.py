import sqlite3
from datetime import datetime

conn = sqlite3.connect("biblioteca.db")

conn.execute("DROP TABLE IF EXISTS emprestimos_livros")

sql_create = """
    CREATE TABLE emprestimos_livros (emprestimo_id INTEGER REFERENCES emprestimos(id),
        livro_id INTEGER REFERENCES livros(id),
        data_devolucao DATE,
        PRIMARY KEY (emprestimo_id, livro_id))
    """
conn.execute(sql_create)

conn.close()
