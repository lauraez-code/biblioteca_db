from usuarios_emprestimos import listar_usuarios, cadastrar_usuario
import sqlite3

while(True):
    print('\n1 - Usuário')
    print('2 - Autores')
    print('3 - Editores')
    print('4 - Livros')
    print('5 - Emprestimos')
    print('6 - Histórico')
    menu = int(input(('Digite: ')))

    if (menu == 1):
        while(True):
            print('\n1 - Cadastrar usuário')
            print('2 - Listar usuários')
            print('3 - Voltar')
            int(input('Digite: '))

            if (menu == 1):
                cadastrar_usuario(sqlite3)
                break

            elif (menu == 2):
                listar_usuarios()
                break

            elif (menu == 3):
                break

            else:
                print('\nAlgo deu errado!\nTente novamente.')

    elif (menu == 2):
        pass

    elif (menu == 3):
        pass

    elif (menu == 4):
        while(True):
            print('\n1 - Cadastrar livro')
            print('2 - Listar livros')
            print('3 - Voltar')
            int(input('Digite: '))

            if (menu == 1):
                pass
                break

            elif (menu == 2):
                pass
                break

            elif (menu == 3):
                break

            else:
                print('\nAlgo deu errado!\nTente novamente.')

    elif (menu == 5):
        while(True):
            print('\n1 - Fazer emprestimo')
            print('2 - Listar emprestimos')
            print('3 - Voltar')
            int(input('Digite: '))

            if (menu == 1):
                pass
                break

            elif (menu == 2):
                pass
                break

            elif (menu == 3):
                break

            else:
                print('\nAlgo deu errado!\nTente novamente.')

    elif (menu == 6):
        pass
        
    else:
        print('\nAlgo deu errado!\nTente novamente.')