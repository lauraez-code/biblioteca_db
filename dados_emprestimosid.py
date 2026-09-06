import sqlite3

conn = sqlite3.connect("biblioteca.db")

conn.execute("DROP TABLE IF EXISTS emprestimos_id")

conn.execute('''
CREATE TABLE emprestimos_id 
(emprestimo_id INTEGER,
livro_id INTEGER,
PRIMARY KEY (emprestimo_id, livro_id),
FOREIGN KEY (emprestimo_id) REFERENCES emprestimos,
FOREIGN KEY (livro_id) REFERENCES livros)''')

conn.executemany("INSERT INTO emprestimos_id(emprestimo_id, livro_id) VALUES (?, ?)", 
                 [(1, 1,), (2, 2,)])

conn.commit()