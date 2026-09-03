# biblioteca_db - Aplicação com Banco de Dados

Implementação do exemplo clássico da Biblioteca salvando em um BAnco de Dados *sqlite*.

As tabelas do projeto são:

**usuarios** (*id, nome*)  
**autores** (*id, nome*)  
**editora** (*id, nome*)  
**livros** (*id, id_autor, titulo, ano_publicacao, editora_id, disponivel*)  
**emprestimos** (*id, usuario_id, data*)  
**emprestimos_id** (*emprestimo_id, livro_id, data_devolucao*)  
