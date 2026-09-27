import sqlite3 as sqlite

# CADASTRANDO 

def cadastrar_livro_autor_editora():

    conn = sqlite.connect("biblioteca.db")
    conn.row_factory = sqlite.Row
    cursor = conn.cursor()

    # Infos livro + autor + editora
    while True:
        disponivel = False
        titulo = input("\nDigite o título do livro: ")
        autor = input("\nDigite o autor do livro: ")
        editora = input("\nDigite a editora do livro: ")
        ano_publicacao = input("\nDigite o ano de publicação do livro: ")
        edicao = input("\nDigite a edição do livro: ")
        disponivel_input = input("Digite 1 para disponível e 2 para indisponível: ")

        if disponivel_input == "1":
            disponivel == True
            print("\n>> Cadastro concluido com sucesso!")
            break

        elif disponivel_input == "2":
            pass
            print("\n>> Cadastro concluido com sucesso!")
            break
        else:
            print("\n>> Digite uma opção válida.")
            
    
    # Verificando se já tem autores

    ja_tem_autor = False

    cursor.execute("SELECT * FROM autores")
    autores = cursor.fetchall()

    for i in autores:
        if i['nome'] == autor:
            ja_tem_autor == True
        else:
            pass

    #Cadastrando autor

    if ja_tem_autor == True:
        pass
    else:
        conn.executemany("INSERT INTO autores(nome) VALUES(?)",
            [(autor,)])
        conn.commit()

    # Verificando se já tem editoras

    ja_tem_editora = False

    cursor.execute("SELECT * FROM editoras")
    editoras = cursor.fetchall()

    for i in editoras:
        if i['nome'] == editora:
            ja_tem_editora == True
        else:
            pass

    #Cadastrando editora

    if ja_tem_editora == True:
            pass
    else:
        conn.executemany("INSERT INTO editoras(nome) VALUES(?)",
            [(editora,)])
        conn.commit()

    #Pegando os id's

    comando_sql1 = "SELECT id FROM autores WHERE nome = ?"
    cursor.execute(comando_sql1, (autor,))
    id_autor = cursor.fetchone

    comando_sql2 = "SELECT id FROM editoras WHERE nome = ?"
    cursor.execute(comando_sql2, (editora,))
    id_editora = cursor.fetchone

    #Cadastrando Livro

    conn.executemany("INSERT INTO livros(titulo, autor_id, editora_id, edicao, ano_publicacao, disponivel) VALUES(?,?,?,?,?,?)",
    (titulo,), (id_autor,), (id_editora,), (edicao,), (ano_publicacao,), (disponivel,))
    conn.commit()

    conn.close()

#LISTANDO

def listar_livros():

    conn = sqlite.connect("biblioteca.db")
    conn.row_factory = sqlite.Row

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM livros")

    livros = cursor.fetchall()

    for linha in livros:
        comando_sql = "SELECT nome FROM autores WHERE = ?"
        cursor.execute(comando_sql, (linha['autor_id']))
        nome_autor = cursor.fetchone
        
        comando_sql2 = "SELECT nome FROM editoras WHERE = ?"
        cursor.execute(comando_sql2, (linha['editora_id']))
        nome_editora = cursor.fetchone


        print(f"\n>> Id: {linha['id']}\n\nTítulo: {linha['titulo']}\n  Autor: {nome_autor}\n  Editora: {nome_editora}\n  Edição: {linha['edicao']}\n  Ano Publicação{linha['ano_publicacao']}")

        if linha['disponivel'] == True:
            print("\n>> Disponível")
        else:
            print("\n>> Indisponível")

    conn.close()

def listar_autores():
    conn = sqlite.connect("biblioteca.db")
    conn.row_factory = sqlite.Row

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM autores")
    autores = cursor.fetchall()

    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()

    for linha in autores:

        print(f"\n>> Id: {linha['id']}\nNome: {linha['nome']}")
        print("\nObras publicadas:")

        for i in livros:
            if i['autor_id'] == linha['id']:
                print(f"\n {i['titulo']}")

    conn.close()

def listar_editoras():
    conn = sqlite.connect("biblioteca.db")
    conn.row_factory = sqlite.Row

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM editoras")
    editoras = cursor.fetchall()

    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()

    for linha in editoras:

        print(f"\n>> Id: {linha['id']}\nNome: {linha['nome']}")
        print("\nObras publicadas:")

        for i in livros:
            if i['editora_id'] == linha['id']:
                print(f"\n {i['titulo']}")

    conn.close()

