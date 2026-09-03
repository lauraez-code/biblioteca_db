import sqlite3

#Conectando o banco de dados. Caso não exista, o banco é criado.
conn = sqlite3.connect("biblioteca.db")

#Apaga a tabela usuários.
conn.execute("DROP TABLE IF EXISTS usuarios")

#Cria a tabela usuários.
conn.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL)")

#Inserindo os registros na tabela usuarios.
conn.executemany("INSERT INTO usuarios(nome) VALUES (?)", 
                 [("Bob",), ("Sam",), ("Frodo",)])

#Confirmando a criação e os inserts da tabela usuarios.
conn.commit()