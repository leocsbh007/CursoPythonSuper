class Pessoa:
    def __init__(self, nome:str, idade:int, peso:float, genero:str) -> None:
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.genero = genero
        
leo = Pessoa('Leonardo', 45, 89.6, 'Homem')

print(leo.genero)
        