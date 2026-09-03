import sqlite3

#Conectando o banco de dados. Caso não exista, o banco é criado.
conn = sqlite3.connect("biblioteca.db")

#Apaga a tabela editoras.
conn.execute("DROP TABLE IF EXISTS editoras")

#Cria a tabela usuários.
conn.execute("CREATE TABLE editoras (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL)")

#Inserindo os registros na tabela usuarios.
conn.executemany("INSERT INTO editoras(nome) VALUES (?)", 
                 [("Moderna",), ("Nova",)])

#Confirmando a criação e os inserts da tabela usuarios.
conn.commit()