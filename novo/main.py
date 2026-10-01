import sqlite3 as sqlite

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








