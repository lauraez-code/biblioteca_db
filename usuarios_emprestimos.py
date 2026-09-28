import sqlite3 as sqlite
from datetime import datetime, timedelta

def cadastrar_usuarios():

    conn = sqlite.connect("biblioteca.db")
    conn.row_factory = sqlite.Row
    cursor = conn.cursor()

    nome = input("\nDigite seu nome de usuário: ")
    senha = input("\nDigite sua senha: ")

    print("\n>> Usuário cadastrado com sucesso!")

    cursor.execute("INSERT INTO usuarios (nome, senha) VALUES (?,?)",
                   (nome, senha,))
    conn.commit()
    conn.close()

def fazer_emprestimo_ver_historico():

    while True:
        conn = sqlite.connect("biblioteca.db")
        conn.row_factory = sqlite.Row
        cursor = conn.cursor()


        nome_usu = input("\nDigite seu nome de usuário: ")
        senha_usu = input("\nDigite sua senha: ")

        tem_usuario = False

        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()

        for i in usuarios:
            if i['nome'] == nome_usu and i['senha'] == senha_usu:
                tem_usuario = True
                usuario_id = i['id']
                break
            else:
                pass

#Fazer emprestimo

        if tem_usuario == True:

            while True:
                print("\n\n============================")
                print(f"\n>> Olá, {nome_usu}!")
                print("\n\n============================")
                print("\n>> O que você deseja fazer hoje?")
                print("\n[1] - Fazer empréstimo")
                print("\n[2] - Ver histórico")
                print("\n[3] - Sair")
                op = input("\n>> Escolha uma opção: ")

                if op == "1":
                    print("\n================= EMPRESTIMO =================")
                    livro = input("\nDigite o nome do livro: ")
                    
                    tem_livro = False
                    tem_estoque = False

                    cursor.execute("SELECT * FROM livros")
                    livros = cursor.fetchall()

                    for i in livros:
                        if i['titulo'] == livro:
                            tem_livro = True
                            if i['estoque'] == 0:
                                pass
                            else:
                                tem_estoque = True
                        else:
                            pass
                    
                    if tem_livro == True and tem_estoque == True:


                        data_hoje = input("\nDigite o dia de hoje (DD/MM/AAAA): ")
                        devolucao = int(input("\nDigite o período do emprestimo em dias: "))

                        comando_sql = "SELECT id FROM livros WHERE titulo = ?"
                        cursor.execute(comando_sql, (livro,))
                        livro_id = cursor.fetchone()[0]

                        data_emprestimo = datetime.strptime(data_hoje, "%d/%m/%Y").date()

                        data_devolucao = data_emprestimo + timedelta(days=devolucao)

                        cursor.execute("INSERT INTO emprestimos (livro_id, usuario_id, data_emprestimo, data_devolucao) VALUES (?,?,?,?)", 
                                    (livro_id, usuario_id, data_emprestimo, data_devolucao,))
                        conn.commit()
                        print("\n>> Emprestimo realizado com sucesso!")
                    
                    elif tem_livro == True and tem_estoque == False:
                        print("\n>> Livro sem estoque!")
                    
                    elif tem_livro == False and tem_estoque == False:
                        print("\n>> Livro não encontrado.")
                    else:
                        pass
                    

                elif op == "2":
                    print(f"\n================= HISTÓRICO DE {nome_usu} =================")
                    cursor.execute("SELECT * FROM emprestimos")
                    emprestimos = cursor.fetchall()

                    for i in emprestimos:

                        if i['usuario_id'] == usuario_id:

                            comando_sql1 = "SELECT titulo FROM livros WHERE id = ?"
                            cursor.execute(comando_sql1, (i['livro_id'],))
                            nome_livro = cursor.fetchone()[0]          

                            print(f"\n Livro: {nome_livro}")
                            print(f" Data de execução do empréstimo: {i['data_emprestimo']}")
                            print("=================")
        

                elif op == "3":
                    break
                        

                else:
                    print("\n>> Digite uma opção válida.")
            
            break
        
        else:
            print("\n>> Usuário ou senha incorretos.")

    conn.close()

#Listar

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

            print(f"\n>> Id: {linha['id']}\nNome: {linha['nome']}")

            print("\nHistórico de empréstimos:")

            for i in emprestimos:
                if i['usuario_id'] == linha['id']:

                    comando_sql1 = "SELECT titulo FROM livros WHERE id = ?"
                    cursor.execute(comando_sql1, (linha['livro_id'],))
                    nome_livro = cursor.fetchone()[0]            

                    print(f"\n Livro: {nome_livro}")
                    print(f" Data de execução do empréstimo: {i['data_emprestimo']}")
                    print(f"Data de devolução: {i['data_devolucao']}")
                    print("====================")
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

            comando_sql2 = "SELECT nome FROM usuarios WHERE id = ?"
            cursor.execute(comando_sql2, (i['usuario_id'],))
            nome_usu = cursor.fetchone()[0]

        
            print(f"\n >> Id: {i['id']}")
            print(f"\nLivro: {nome_livro}")
            print(f"Usuário: {nome_usu}")
            print(f"Data do empréstimo: {i['data_emprestimo']}")
            print(f"Data devolução: {i['data_devolucao']}")
            print("\n====================\n")
    
        conn.close()






