class Calculadora:
    def __init__(self) -> None:
        self.soma = 0
        self.subtracao = 0
        self.multiplicacao = 0
        self.divisao = 0
        
    def somar(self, num1, num2):
        self.soma = num1 + num2
        print(f'{num1} + {num2} = {self.soma}')
    
    def subtrair(self, num1, num2):
        self.subtracao = num1 - num2
        print(f'{num1} - {num2} = {self.subtracao}')
    
    def multiplicar(self, num1, num2):
        self.multiplicacao = num1 * num2
        print(f'{num1} * {num2} = {self.multiplicacao}')
    
    def dividir(self, num1, num2):
        if num2 == 0:
            
            print(f'{num1} / {num2} = Erro')
        else:    
            self.divisao = num1 / num2
            print(f'{num1} / {num2} = {self.divisao}')    
    
        

