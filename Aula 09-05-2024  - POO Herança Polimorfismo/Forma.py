
# Perímetro do retângulo => 2 x (l maior + lado menor)
# Perímetro do quadrado =>  l + l + l + l = 4 x l
# 



class Forma:
    def __init__(self, nome:str) -> None:
        self.nome = nome

    
class Quadrado(Forma):
    def __init__(self, nome) -> None:
        super().__init__(nome)
    
    def calcular_perimetro(self, lado) -> float:
        perimetro = 4 * lado        
        return perimetro
    
class Retangulo(Forma):
    def __init__(self, nome) -> None:
        super().__init__(nome)
    
    def calcular_perimetro(self, lado1 : float, lado2 : float) -> float:
        perimetro = 2 * (lado1 + lado2)
        return perimetro
    
