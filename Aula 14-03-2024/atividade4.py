# ATIVIDADE PRÁTICA 4

# Crie uma função que receba dois números e retorne a
# subtração do primeiro pelo segundo.

def subtrai_dois_numeros(num1: float, num2: float) -> float:
    '''
    RECEBE DOIS NUMEROS COMO PARAMETRO E RETORNA A SUBTRAÇAO DO PRIMEIRO NUMERO PELO SEGUNDO
    '''
    resultado = num1 - num2
    return resultado

numero1 = float(input('Entre com o primeiro numero: '))
numero2 = float(input('Entre com o segundo numero: '))

print(f'A subtração de {numero1} - {numero2} = {subtrai_dois_numeros(numero1,numero2)}')