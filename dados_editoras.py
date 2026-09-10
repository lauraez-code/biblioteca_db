import sqlite3

conn = sqlite3.connect("biblioteca.db")

#apaga a tabela editoras
conn.execute("DROP TABLE IF EXISTS editoras")

#cria a tabela editoras
conn.execute("CREATE TABLE editoras (id INTEGER PRIMARY KEY AUTOINCREMENT \
             , nome TEXT NOT NULL)")

#inserindo os registros na tabela editoras
conn.executemany("INSERT INTO editoras(nome) VALUES(?)",
                 [("Moderna",), ("Nova",)])

#confirmando a criação e os inserts da tabela editoras.
conn.commit()