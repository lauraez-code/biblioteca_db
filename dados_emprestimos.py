import sqlite3

conn = sqlite3.connect("biblioteca.db")

conn.execute("DROP TABLE IF EXISTS emprestimos")

conn.execute("CREATE TABLE emprestimos (id INTEGER PRIMARY KEY AUTOINCREMENT, data DATE NOT NULL, id_usuario INTEGER REFERENCES usuario(id))")

conn.executemany("INSERT INTO emprestimos(data, id_usuario) VALUES (?, ?)", 
                 [('03-02-2026', 1), ("04-06-2026", 2,)])

conn.commit()