def ola_mundo():
    print('Ola Mundo')

def soma_dois_numeros(num1:float, num2:float):
    '''
    ESTA FUNÇÃO RECEBE DOIS PARAMETROS E EFETUA A SOMA
    num1 -> Recebe o primeiro parametro
    num2 -> Recebe o segundo parametro
    '''
    soma = num1 + num2
    return soma

resultado = soma_dois_numeros(10,20)
print(resultado)

