def soma(num1 : int, num2 : int) -> int:
    
    resultado = num1 + num2
    return resultado


def subtracao(num1 : int, num2 : int) -> int:
    
    resultado = num1 - num2
    return resultado

def multiplicacao(num1 : int, num2 : int) -> int:
    
    resultado = num1 * num2
    return resultado


def divisao(num1 : int, num2 : int) -> int:
    
    if num2 == 0:
        return 'Erro'
    else: 
        resultado = num1 / num2
        return resultado

bola = 10
metal = 20

