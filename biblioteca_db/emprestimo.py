import sqlite3 as sqlite

from datetime import datetime, timedelta


def fazer_emprestimo(email_usuario):

    conn = sqlite.connect("biblioteca.db")
    conn.row_factory = sqlite.Row
    cursor = conn.cursor()    

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

        cursor.execute("INSERT INTO emprestimos (livro_id, usuario_email, data_emprestimo, data_devolucao) VALUES (?,?,?,?)", 
            livro_id, email_usuario, data_emprestimo, data_devolucao,)
        conn.commit()
        
        print("\n>> Emprestimo realizado com sucesso!")

        comando_sql8 = "SELECT estoque FROM livros WHERE id = ?"
        cursor.execute(comando_sql8, (livro_id,))
        estoque_livro = cursor.fetchone()[0]

        comando_sql5 = "UPDATE livros SET estoque = ? WHERE id = ?"
        cursor.execute(comando_sql5, (estoque_livro - 1, livro_id,))
        conn.commit()

                            
    elif tem_livro == True and tem_estoque == False:
        print("\n>> Livro sem estoque!")
                            
    elif tem_livro == False and tem_estoque == False:
        print("\n>> Livro não encontrado.")

    else:
        pass