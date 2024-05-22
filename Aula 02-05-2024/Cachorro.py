class Cachorro:
    def __init__(self, nome:str, raca:str, idade:int) -> None:
        self.nome = nome
        self.raca = raca
        self.idade = idade
        

dog = Cachorro('João','Yorshire', 10)

print(dog.nome)