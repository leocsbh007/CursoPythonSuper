class Animal:
    def __init__(self, nome: str):
        self.nome = nome

    def saudar_animal(self):
        print('Olááá sou um animal.')

class Gato(Animal):
    def __init__(self, nome: str, brinca_la: bool):
        super().__init__(nome)
        self.brinca_la = brinca_la

    def saudacao(self):
        super().saudar_animal()
        print('miau miau miau')


nome = 'Felix'
gato = Gato(nome, True)
print(vars(gato))
gato.saudacao()