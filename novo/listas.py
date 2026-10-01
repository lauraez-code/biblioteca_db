import sqlite3 as sqlite

def listar_livros():

    conn = sqlite.connect("biblioteca.db")
    conn.row_factory = sqlite.Row

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM livros")

    livros = cursor.fetchall()

    if len(livros) == 0:
        print("\n>> Não há livros cadastrados!")
    else:

        for linha in livros:
            comando_sql = "SELECT nome FROM autores WHERE id = ?"
            cursor.execute(comando_sql, (linha['autor_id'],))
            nome_autor = cursor.fetchone()[0]
            
            comando_sql2 = "SELECT nome FROM editoras WHERE id = ?"
            cursor.execute(comando_sql2, (linha['editora_id'],))
            nome_editora = cursor.fetchone()[0]


            print(f"\nTítulo: {linha['titulo']}\n\n  >> Id: {linha['id']}\n\n\n  Autor: {nome_autor}\n  Editora: {nome_editora}\n  Edição: {linha['edicao']}\n  Ano Publicação: {linha['ano_publicacao']}\n  Estoque: {linha['estoque']}")

            print("\n====================\n")

    conn.close()


def listar_autores():
    conn = sqlite.connect("biblioteca.db")
    conn.row_factory = sqlite.Row

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM autores")
    autores = cursor.fetchall()

    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()

    if len(autores) == 0:
        print("\n>> Não há autores cadastrados!")

    else:

        for linha in autores:

            print(f"\n>> Id: {linha['id']}\nNome: {linha['nome']}")
            print("\nObras publicadas:")

            for i in livros:
                print("= = = = = = = =")
                if i['autor_id'] == linha['id']:
                    print(f"\n {i['titulo']}")
                    print("= = = = = = = =")
            print("\n====================\n")

    conn.close()


def listar_editoras():
    conn = sqlite.connect("biblioteca.db")
    conn.row_factory = sqlite.Row

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM editoras")
    editoras = cursor.fetchall()

    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()

    if len(editoras) == 0:
        print("\n>> Não há editoras cadastradas!")

    else:

        for linha in editoras:

            print(f"\n>> Id: {linha['id']}\nNome: {linha['nome']}")
            print("\nObras publicadas:")

            for i in livros:
                if i['editora_id'] == linha['id']:
                    print(f"\n {i['titulo']}")
                    

    conn.close()


def listar_usuarios():

    conn = sqlite.connect("biblioteca.db")
    conn.row_factory = sqlite.Row

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    cursor.execute("SELECT * FROM emprestimos")
    emprestimos = cursor.fetchall()

    if len(usuarios) == 0:
        print("\n>> Não há usuários cadastrados!")
    else:

        for linha in usuarios:

            print(f"\n>> Email: {linha['email']}\nNome: {linha['nome']}")
            print("\n====================\n")

    conn.close()


def listar_emprestimos():

    conn = sqlite.connect("biblioteca.db")
    conn.row_factory = sqlite.Row

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM emprestimos")
    emprestimos = cursor.fetchall()

    if len(emprestimos) == 0:
        print("\n>> Não há emprestimos registrados!")
    else:

        for i in emprestimos:
            
            comando_sql = "SELECT titulo FROM livros WHERE id = ?"
            cursor.execute(comando_sql, (i['livro_id'],))
            nome_livro = cursor.fetchone()[0]

            comando_sql2 = "SELECT nome FROM usuarios WHERE email = ?"
            cursor.execute(comando_sql2, (i['usuario_email'],))
            email_usu = cursor.fetchone()[0]

        
            print(f"\n >> Id: {i['id']}")
            print(f"\nLivro: {nome_livro}")
            print(f"Usuário: {email_usu}")
            print(f"Data do empréstimo: {i['data_emprestimo']}")
            print(f"Data devolução: {i['data_devolucao']}")
            print("\n====================\n")
    
        conn.close()


def listar_historico_usuario():

    conn = sqlite.connect("biblioteca.db")
    conn.row_factory = sqlite.Row

    cursor = conn.cursor()
            
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    cursor.execute("SELECT * FROM emprestimos")
    emprestimos = cursor.fetchall()    
    
    tem_historico = False

    for linha in usuarios:
        
        for i in emprestimos:
            if i['usuario_email'] == linha['email']:
                tem_historico = True
                comando_sql1 = "SELECT titulo FROM livros WHERE id = ?"
                cursor.execute(comando_sql1, (i['livro_id'],))
                nome_livro = cursor.fetchone()[0]            

                print(f"\n Livro: {nome_livro}")
                print(f" Data de execução do empréstimo: {i['data_emprestimo']}")
                print(f" Data de devolução: {i['data_devolucao']}")
                print("\n====================")
                
                if tem_historico == True:
                    pass
                else:
                    print("\n>> Usuário sem histórico.")
        
    conn.close()