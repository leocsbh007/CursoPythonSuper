class Livro:
    def __init__(self, titulo, autor, id) -> None:
        self.__titulo = titulo
        self.__autor = autor
        self.__id = id
        # True esta disponivel para locação
        # False NÃO esta disponivel para locação
        self.__staus_locacao = True
        
    @property
    def titulo(self):
        return self.__titulo
        
    @property
    def autor(self):
        return self.__autor
    
    @property
    def id(self):
        return self.__id
    
    @property
    def status_locacao(self):
        return self.__staus_locacao
    
    @titulo.setter
    def titulo(self, novo_titulo):
        self.__titulo = novo_titulo
        
    @autor.setter
    def autor(self,novo_titulo):
        self.__autor = novo_titulo
    
    @id.setter
    def id(self, novo_id):
        self.__id = novo_id
    
    @status_locacao.setter
    def status_locacao(self, novo_status):
        self.__staus_locacao = novo_status
    
    
    
class Membro:
    def __init__(self, nome, numero_membro):
        self.__nome = nome
        self.__numero_membro = numero_membro
        self.__historico = []
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def numero_membro(self):
        return self.__numero_membro
    
    @property
    def historico(self) -> list:
        return self.__historico
                

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
        
    @numero_membro.setter
    def numero_membro(self, novo_numero_membro):
        self.__numero_membro = novo_numero_membro
    
    @historico.setter
    def historico(self, livro):
        self.__historico.append(livro)
        
    def adicionar_livro(self, livro:Livro):
        self.__historico.append(livro)
        
    def exibir_livros(self):
        for livro in self.__historico:
            print(f"Id: {livro.id}")
            print(f"Titulo: {livro.titulo}")
            print(f"Autor: {livro.autor}")
            print(f"Disponivel: {livro.status_locacao}")
            print('='*40)
            
class Biblioteca:
    def __init__(self) -> None:
        self.__catalogo = []
        self.__membros = []
        
    def adicionar_livro(self, livro : Livro):
        self.__catalogo.append(livro)
        
    def adicionar_membro(self, membro : Membro):
        self.__membros.append(membro)
        
    def permitir_emprestimo(self, membro : Membro, livro : Livro):
        livro.status_locacao = False
        membro.adicionar_livro(livro)
    
    def regitra_devolucao(self, livro : Livro):
        livro.status_locacao = True
        
    def pesquisar_livros(self, id):
        if len(self.__catalogo) == 0:
            print('O Catalogo de livros esta vazio')
        for i in range(len(self.__catalogo)):
            if id == self.__catalogo[i].id:
                print(f"Id: {self.__catalogo[i].id}")
                print(f"Titulo: {self.__catalogo[i].titulo}")
                print(f"Autor: {self.__catalogo[i].autor}")
                print(f"Disponivel: {self.__catalogo[i].status_locacao}")
                print('='*40)
                
                
        
    
        
    
        
            
            
    