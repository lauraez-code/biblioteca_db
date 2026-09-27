import sqlite3 as sqlite

def cadastrar_usuario(sqlite3):
    conn = sqlite3.connect("biblioteca.db")
   
    nome_usuario = input('\nDigite o nome do usuário: ')

    conn.execute("INSERT INTO usuarios(nome) VALUES(?)", (nome_usuario,))

    print('\nUsuário adicionado com sucesso!')
   
    conn.commit()
   
def listar_usuarios():
    #abre uma conexão com o banco
    conn = sqlite.connect("biblioteca.db")
    conn.row_factory = sqlite.Row

    #cria um cursor (um objeto para interagir com o banco)
    cursor = conn.cursor()

    #executa o sql
    cursor.execute("SELECT * FROM usuarios")

    #pega os registros e guarda na variável resultados
    resultados = cursor.fetchall()

    #percorre os registros que retornaram
    for linha in resultados:
        print(f"id: {linha['id']} | nome: {linha['nome']}")

    #fecha a conexão
    conn.close()
