import sqlite3 as sqlite

from biblioteca_db.usuarios import cadastrar_usuarios, fazer_login


conn = sqlite.connect("biblioteca.db")
conn.row_factory = sqlite.Row
cursor = conn.cursor()



while True:

    print("\n\n============= BIBLIOTECA =============")
    print("\n[1] - Fazer login")
    print("\n[2] - Não tem conta? Cadastre-se")
    print("\n[3] - Sair")

    menu = input("\n>> Digite uma opção: ")

    if menu == '1':
        fazer_login()

    elif menu == '2':
        cadastrar_usuarios()

    elif menu == '3':
        break

    else:
        print("\n>> Digite uma opção válida!")

    pass








