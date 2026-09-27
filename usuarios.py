import sqlite3 as sqlite
from datetime import datetime, timedelta

def cadastrar_usuarios(nome, senha):

    conn = sqlite.connect("biblioteca.db")
    conn.row_factory = sqlite.Row
    cursor = conn.cursor()

    nome = input("\nDigite seu nome de usuário: ")
    senha = input("\nDigite sua senha: ")

    print("\n>> Usuário criado com sucesso!")

    cursor.execute("INSERT INTO usuarios VALUES (?)",
                   (nome,), (senha,))
    conn.commit()
    conn.close()

def fazer_emprestimo_ver_historico():

    while True:
        conn = sqlite.connect("biblioteca.db")
        conn.row_factory = sqlite.Row
        cursor = conn.cursor()

        nome_usu = input("\nDigite seu nome de usuário: ")
        senha_usu = input("Digite sua senha: ")

        tem_usuario = False

        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall

        for i in usuarios:
            if i['nome'] == nome_usu and i['senha'] == senha_usu:
                tem_usuario = True
                usuario_id = i['id']
                break
            else:
                pass

#Fazer emprestimo

        if tem_usuario == True:

            print(f"\n\n>> Olá, {nome_usu}!")

            while True:

                print("\n[1] - Fazer empréstimo")
                print("\n[2] - Ver histórico")
                print("\n[3] - Sair")
                op = input("\n>> Escolha uma opção: ")

                if op == "1":

                    livro = input("\nDigite o nome do livro: ")
                    data_hoje = input("\nDigite o dia de hoje (DD/MM/AAAA): ")
                    devolucao = int(input("Digite o período do emprestimo em dias: "))

                    comando_sql = "SELECT id FROM livros WHERE titulo = ?"
                    cursor.execute(comando_sql, (livro,))
                    livro_id = cursor.fetchone

                    data_emprestimo = datetime.strptime(data_hoje, "%d/%m/%Y").date()

                    nova_data = data_emprestimo + timedelta(days=devolucao)

                    data_devolucao = datetime.strptime(nova_data, "%d/%m/%Y").date()

                    cursor.execute("INSERT INTO emprestimos (livro_id, usuario_id, data_emprestimo, data_devolucao) VALUES (?,?,?,?)", 
                                   (livro_id,), (usuario_id,), (data_emprestimo,), (data_devolucao,))
                    conn.commit()
                    

                elif op == "2":
                    cursor.execute("SELECT * FROM emprestimos")
                    emprestimos = cursor.fetchall

                    for i in emprestimos:

                        if i['id_usuario'] == usuario_id:

                            comando_sql1 = "SELECT titulo FROM livros WHERE id = ?"
                            cursor.execute(comando_sql1, (i['livro_id'],))
                            nome_livro = cursor.fetchone            

                            print(f"\n Livro: {nome_livro}")
                            print(f" Data de execução do empréstimo: {i['data_emprestimo']}")

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
    emprestimos = cursor.fetchall

    for linha in usuarios:

        print(f"\n>> Id: {linha['id']}\n\nNome: {linha['nome']}")

        print("\nHistórico de empréstimos:")

        for i in emprestimos:
            if i['id_usuario'] == linha['id']:

                comando_sql1 = "SELECT titulo FROM livros WHERE id = ?"
                cursor.execute(comando_sql1, (linha['livro_id'],))
                nome_livro = cursor.fetchone            

                print(f"\n Livro: {nome_livro}")
                print(f" Data de execução do empréstimo: {i['data_emprestimo']}")
            
    conn.close()

def listar_emprestimos():

    conn = sqlite.connect("biblioteca.db")
    conn.row_factory = sqlite.Row

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    cursor.execute("SELECT * FROM emprestimos")
    emprestimos = cursor.fetchall

    for i in emprestimos:
        pass
            
    conn.close()






