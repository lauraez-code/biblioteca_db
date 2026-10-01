import sqlite3 as sqlite

def cadastrar_livro_autor_editora():

    conn = sqlite.connect("biblioteca.db")
    conn.row_factory = sqlite.Row
    cursor = conn.cursor()

    # Infos livro + autor + editora
    titulo = input("\nDigite o título do livro: ")
    autor = input("\nDigite o autor do livro: ")
    editora = input("\nDigite a editora do livro: ")
    ano_publicacao = input("\nDigite o ano de publicação do livro: ")
    edicao = input("\nDigite a edição do livro: ")
    estoque = input("\nDigite o estoque do livro: ")          
    
    # Verificando se já tem autores

    ja_tem_autor = False

    cursor.execute("SELECT * FROM autores")
    autores = cursor.fetchall()

    for i in autores:
        if i['nome'] == autor:
            ja_tem_autor = True
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
            ja_tem_editora = True
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
    id_autor = cursor.fetchone()[0]

    comando_sql2 = "SELECT id FROM editoras WHERE nome = ?"
    cursor.execute(comando_sql2, (editora,))
    id_editora = cursor.fetchone()[0]

    #Cadastrando Livro

    conn.execute("INSERT INTO livros (titulo, autor_id, editora_id, edicao, ano_publicacao, estoque) VALUES(?,?,?,?,?,?)",
    (titulo, id_autor, id_editora, edicao, ano_publicacao, estoque,))
    conn.commit()

    conn.close()

