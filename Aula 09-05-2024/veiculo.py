class Veiculo:
    def __init__(self, cor: str, modelo: str, tipo: str) -> None:
        self.cor = cor
        self.modelo = modelo
        self.tipo = tipo
        
    def mostra_cor_modelo(self):
        print(f'Mostrando Modelo e Cor do {self.tipo}')        
        print(f'Modelo : {self.modelo}  - Cor:  {self.cor}')
        print('='*20)
      
class Carro(Veiculo):
    def __init__(self, cor: str, modelo: str, tipo: str) -> None:
        super().__init__(cor, modelo, tipo)
        
        
        
    def alterar_cor (self, nova_cor: str) -> None:
        self.cor = nova_cor
        
    def alterar_modelo (self, novo_modelo: str) -> None:
        self.modelo = novo_modelo        
   
        
        
class Bicicleta(Veiculo):
    def __init__(self, cor: str, modelo: str, tipo: str) -> None:
        super().__init__(cor, modelo, tipo)
        
    def alterar_cor (self, nova_cor: str) -> None:
        self.cor = nova_cor
        
    def alterar_modelo (self, novo_modelo: str) -> None:
        self.modelo = novo_modelo
        