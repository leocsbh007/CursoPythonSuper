class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade
        
class Estudante(Pessoa):
    def __init__(self, nome: str, idade: int, curso: str) -> None:
        super().__init__(nome, idade)
        self.curso = curso
        
class Professor(Pessoa):
    def __init__(self, nome: str, idade: int, disciplina: str) -> None:
        super().__init__(nome, idade)
        self.disciplina = disciplina
        
    def altera_disciplina(self, nova_disciplina):
        self.disciplina = nova_disciplina