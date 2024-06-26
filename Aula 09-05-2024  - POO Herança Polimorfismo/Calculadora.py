'''
ATIVIDADE PRÁTICA 3

Crie uma classe chamada "Calculadora" com um método "somar" que pode somar dois números inteiros ou duas
strings. Use o polimorfismo para implementar a sobrecarga do método "somar"
para que ele funcione com diferentes tipos de entrada (números inteiros e strings).
Crie exemplos de uso para demonstrar como a mesma função pode se comportar de maneira diferente
com base nos tipos de entrada.


'''
class Calculadora:
    def somar(self):
        pass
    
class Soma_Inteiro(Calculadora):
    def somar(self, num1: int, num2:int) -> int:
        soma = num1 + num2
        return soma

class Soma_String(Calculadora):
    def somar(self, num1: str, num2:str) -> str:
        soma = int(num1) + int(num2)
        return str(soma)

def somando(soma):
    return soma.somar()