# DESAFIO PRÁTICO

# Calculadora
# Crie uma calculadora com opções de soma, multiplicação, subtração,
# divisão e sair.
# (Ela deverá funcionar infinitamente, até que o usuário decida sair da
# calculadora.)
# Utilize funções de rotina para cada operação e funções de unidade
# lógica para realizar os cálculos.
# Dica:
# Utilize de condicionais e Laços de Repetição para realizar esse
# exercício.

def soma(num1: float, num2: float) -> float:
    return num1 + num2

def subtracao(num1: float, num2: float) -> float:
    return num1 - num2

def multiplicacao(num1: float, num2: float) -> float:
    return num1 * num2

def divisao(num1: float, num2: float) -> float:    
    return num1 / num2


controle = True
numero1 = 0
numero2 = 0

while controle:
    numero1 = float(input('Entre com o primeiro numero: '))
    numero2 = float(input('Entre com o segundo numero: '))
    
    print('''
          
            QUAL OPERAÇÃO VOCÊ QUER FAZER?
            ( + ) - ADIÇÃO
            ( - ) - SUBTRAÇÃO
            ( * ) - MULTIPLICAÇÃO
            ( / ) - DIVISÃO
            ( # ) - SAI DA CALCULADORA
          
          ''')
    operacao = input('Qual operação você quer fazer? ')
    match operacao:
        case '+':
            print(f'RESULTADO - {numero1} + {numero2} = {soma(numero1, numero2)}')
        case '-':
            subtracao(numero1, numero2)
        case '*':
            multiplicacao(numero1, numero2)
        case '/':      
            if numero2 == 0:
                print('ERRO')      
            else:
                divisao(numero1, numero2)
        case '#':
            controle = False
    print('Deseja continuar? ')
    
            
else: 
    print('Saindo da Calculadora')
            



