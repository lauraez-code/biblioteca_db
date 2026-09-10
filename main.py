import sqlite3 as sqlite

#abre uma conexão com o banco
conn = sqlite.connect("biblioteca.db")

#cria um cursor (um objeto para interagir com o banco)
cursor = conn.cursor()

#executa o sql
cursor.execute("SELECT * FROM usuarios")

#pega os registros e guarda na variável resultados
resultados = cursor.fetchall()

#percorre os registros que retornaram
for linha in resultados:
    print(f"id: {linha[0]} | nome: {linha[1]}")

#fecha a conexão
conn.close()