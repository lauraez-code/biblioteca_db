import sqlite3 as sqlite

def fazer_emprestimo():

    conn = sqlite.connect("biblioteca.db")
    conn.row_factory = sqlite.Row

    cursor = conn.cursor()

    #livro_id, usuario_id, data_emprestimo, data_devolução

    input("")