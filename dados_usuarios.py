import sqlite3

#conectando o banco de dados. Caso não exista, o banco é criado.
conn = sqlite3.connect("biblioteca.db")

conn.execute("DROP TABLE usuarios")

#cria a tabela usuarios
conn.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT \
             , nome TEXT NOT NULL)")

#confirmando a criação e os inserts da tabela usuarios.
conn.commit()