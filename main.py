import sqlite3 as sqlite

conn = sqlite.connect("biblioteca.db")
conn.row_factory = sqlite.Row
cursor = conn.cursor()

from livros_autores_editoras import cadastrar_livro_autor_editora, listar_autores, listar_editoras, listar_livros
from usuarios_emprestimos import cadastrar_usuarios, fazer_emprestimo_ver_historico, listar_emprestimos, listar_usuarios

while True:

    print("\n\n====================== BIBLIOTECA =======================")
    print("\n[1] - Livros")
    print("\n[2] - Autores")
    print("\n[3] - Editoras")
    print("\n[4] - Usuários")

    menu = input("\n>> Escolha uma opção: ")

    if menu == "1":

        while True:
            print("\n\n============== LIVROS ==============")
            print("\n[1] - Fazer empréstimo")
            print("\n[2] - Cadastrar livro")
            print("\n[3] - Ver livros")
            print("\n[4] - Histórico de empréstimos")
            print("\n[5] - Sair")

            op = input("\n>> Escolha uma opção: ")

            if op == "1":
                while True:
                    print("\n[1] - Fazer login")
                    print("\n[2] - Não tem conta? Cadastre-se")
                    print("\n[3] - Sair")
                
                    opp = input("\n>> Escolha uma opção: ")

                    if opp == "2":
                        print("\n\n============== CADASTRANDO USUÁRIO ==============")
                        cadastrar_usuarios()

                    elif opp == "1":
                        print("\n\n============================")
                        print("\n>> Login:\n")
                        fazer_emprestimo_ver_historico()

                    elif opp == "3":
                        break
                    else:
                        print("\n>> Digite uma opção válida")

            elif op == "2":
                print("\n\n============== CADASTRANDO LIVRO ==============")
                cadastrar_livro_autor_editora()

            elif op == "3":
                print("\n\n============== LIVROS CADASTRADOS ==============")
                listar_livros()

            elif op == "4":
                print("\n\n============== HISTÓRICO DE EMPRÉSTIMOS ==============")
                listar_emprestimos()

            elif op == "5":
                break
            else:
                print("\n>> Digite uma opção válida.")

    elif menu == "2":
        print("\n\n============== AUTORES ==============")
        listar_autores()

    elif menu == "3":
        print("\n\n============== EDITORAS ==============")
        listar_editoras()

    elif menu == "4":
        print("\n\n============== USUÁRIOS ==============")
        listar_usuarios()







