import sqlite3 as sqlite

def cadastrar_livro(titulo, autor_id, editora_id, ano_publicacao, edicao, disponivel):

    conn = sqlite.connect("biblioteca.db")
    conn.row_factory = sqlite.Row
    cursor = conn.cursor()

    # Cadastrando livro

    disponivel = False
    titulo = input("\nDigite o título do livro: ")
    autor = input("\nDigite o autor do livro: ")
    editora = input("\nDigite a editora do livro: ")
    ano_publicacao = input("\nDigite o ano de publicação do livro: ")
    edicao = input("\nDigite a edição do livro: ")
    disponivel_input = input("Digite 1 para disponível e 2 para indisponível: ")

    # Verificando se já tem autores

    ja_tem_autor = False

    cursor.execute("SELECT * FROM autores")
    autores = cursor.fetchall()

    for i in autores:
        if i['nome'] == autor:
            ja_tem_autor == True
            id_autor = i['id']
        else:
            pass

    if ja_tem_autor == True:
        pass
    else:
        conn.executemany("INSERT INTO autores(nome) VALUES(?)",
            [(autor,)])

    # Verificando se já tem editoras

    ja_tem_editora = False

    cursor.execute("SELECT * FROM editoras")
    editoras = cursor.fetchall()

    for i in editoras:
        if i['nome'] == editora:
            ja_tem_editora == True
            id_editora = i['id']
        else:
            pass

    if ja_tem_editora == True:
            pass
    else:
        conn.executemany("INSERT INTO editoras(nome) VALUES(?)",
            [(editora,)])

    comando_sql = "SELECT id FROM autores WHERE id = ?"
    cursor.execute(comando_sql, (autor,))
    linha = cursor.fetchone

    comando_sql = "SELECT id FROM editoras WHERE id = ?"
    cursor.execute(comando_sql, (editora,))
    linha2 = cursor.fetchone




    #Cadastrando Livro

    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()

    for i in livros:






        ''

        i

    conn.executemany("INSERT INTO livros(titulo, autor_id, editora_id, edicao, disponivel) VALUES(?,?,?,?,?)",
    )