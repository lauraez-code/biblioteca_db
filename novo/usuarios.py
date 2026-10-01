import sqlite3 as sqlite

def cadastrar_usuarios():

    conn = sqlite.connect("biblioteca.db")
    conn.row_factory = sqlite.Row
    cursor = conn.cursor()

    while True:

        print("\n>> Digite 0 caso deseje sair dessa página.")
        nome = input("\nDigite seu nome de usuário: ")
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")

        if nome == '0' or email == '0' or senha == '0':
            break
        
        else:
            cursor.execute("SELECT * FROM usuarios")
            usuarios = cursor.fetchall() 

            ja_tem = False

            for i in usuarios:
                if i['email'] == email:
                    ja_tem = True
                else:
                    pass   

            if ja_tem == True:
                print("\n>> Email já cadastrado. Por favor, altere o email ou digite sua senha corretamente.")

            else:

                print("\n>> Usuário cadastrado com sucesso!")

                cursor.execute("INSERT INTO usuarios (nome, senha, email) VALUES (?,?,?)",
                            (nome, senha, email))
                conn.commit()
        
    conn.close()

def fazer_login():
    
    conn = sqlite.connect("biblioteca.db")
    conn.row_factory = sqlite.Row
    cursor = conn.cursor()

    while True:
        print("\n>> Digite 0 caso deseja sair dessa aba.")
        email_usu = input("\nDigite seu email: ")
        senha_usu = input("\nDigite sua senha: ")

        if email_usu == '0' or senha_usu == '0':
            break
            
        else:

            if email_usu == 'root@email' and senha_usu == 1234:
                menu_root()
            
            else:

                tem_usuario = False

                cursor.execute("SELECT * FROM usuarios")
                usuarios = cursor.fetchall()

                for i in usuarios:
                    if i['email'] == email_usu and i['senha'] == senha_usu:
                        tem_usuario = True
                        break
                    else:
                        pass
        
    if tem_usuario == True:
        menu_usuario()
    
    else:
        print("\n>> Usuário não encontrado.")
    
    conn.close()

def menu_usuario(email_usu):

    conn = sqlite.connect("biblioteca.db")
    conn.row_factory = sqlite.Row
    cursor = conn.cursor()    

    comando = "SELECT nome FROM usuarios WHERE email = ?"
    cursor.execute(comando, (email_usu,))
    nome_usu = cursor.fetchone()[0]

    while True:

        print("\n============= BIBLIOTECA =============")
        print(f"\n>> Olá, {nome_usu}! O que gostaria de fazer hoje?")
        print("\n[1] - Fazer empréstimo")
        print("[2]- Ver histórico")
        print("[3] - Sair")

        menu = input("\n>> Digite uma opção: ")

        if menu == '1':
            fazer_emprestimo()
        
        elif menu == '2':
            ver_historico()
        
        elif menu == '3':
            break
        
        else:
            print("\n>> Digite uma opção válida.")
        
        conn.close()

def menu_root():

    conn = sqlite.connect("biblioteca.db")
    conn.row_factory = sqlite.Row
    cursor = conn.cursor()    

    while True:

        print("\n============= ADM - BIBLIOTECA =============")
        print("\n>> Olá ADM! O que gostaria de fazer hoje?")
        print("\n[1] - Livros")
        print("[2] - Usuários")
        print("[3] - Editoras")
        print("[4] - Autores")
        print("[5] - Sair")
    
        menu = input("\n>> Digite uma opção: ")

        if menu == "1":

            while True:

                print("\n============= LIVROS =============")
                print("\n[1] - Cadastrar livro")
                print("[2] - Listar livros")
                print("[3] - Sair")

                op = input("\n>> Digite uma opção: ")

                if op == '1':
                    cadastrar_livro()
                
                elif op == '2':
                    listar_livros()
                
                elif op == '3':
                    break

                else:
                    print("\n>> Digite uma opção válida.")
        
        elif menu == "2":
  
            while True:

                print("\n============= USUARIOS =============")
                print("\n[1] - Listar usuario")
                print("[2] - Ver histórico do usuário")
                print("[3] - Sair")

                opp = input("\n>> Digite uma opção: ")

                if opp == '1':
                    listar_usuarios()
                
                elif opp == '2':
                    ver_historico_usuario()
                
                elif opp == '3':
                    break
                
                else:
                    print("\n>> Digite uma opção válida.")
        
        elif menu == '3':
            listar_editoras()
        
        elif menu == '4':
            listar_autores()
        
        elif menu == '5':
            break
        
        else:
            print("\n>> Digite uma opção válida.")
    
    conn.close()


        






            




        


