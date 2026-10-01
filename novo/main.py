import sqlite3 as sqlite

conn = sqlite.connect("biblioteca.db")
conn.row_factory = sqlite.Row
cursor = conn.cursor()

from livros_autores_editoras import cadastrar_livro_autor_editora, listar_autores, listar_editoras, listar_livros
from usuarios_emprestimos import cadastrar_usuarios, fazer_emprestimo_ver_historico, listar_emprestimos, listar_usuarios

while True:

    print("\n\n============= BIBLIOTECA =============")
    print("\n[1] - Fazer login")
    print("\n[2] - Não tem conta? Cadastre-se")
    print("\n[3] - Sair")

    menu = input("\n>> Digite uma opção: ")

    if menu == '1':
        fazer_login()
        







