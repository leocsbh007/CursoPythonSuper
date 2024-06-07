from biblioteca import *

livro1 = Livro('De volta ao futuro', 'Leonardo', '001')
livro2 = Livro('E ai como foi o feriado', 'Jose', '002')
livro3 = Livro('Programação para leigos', 'Manoel', '003')

# print(livro.autor, livro.status_locacao, livro.titulo)
# livro.autor ='Antonio'
# livro.titulo ='As voltas que a vida dá'
# print(livro.autor, livro.titulo)

membro1 = Membro('Leonardo','001')
membro1.adicionar_livro(livro1)
membro1.adicionar_livro(livro2)
membro1.adicionar_livro(livro3)

# usuario.exibir_livros()

biblioteca = Biblioteca()
# biblioteca.pesquisar_livros('De volta ao futuro')
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

biblioteca.adicionar_membro(membro1)
biblioteca.permitir_emprestimo(membro1,livro1)

biblioteca.pesquisar_livros('001')

biblioteca.regitra_devolucao(livro1)

biblioteca.pesquisar_livros('001')



