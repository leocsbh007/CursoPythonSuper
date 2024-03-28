'''
ATIVIDADE PRÁTICA 2
Crie um programa que define uma função
calcular_area_retangulo que recebe dois argumentos,
comprimento e largura de um retângulo, e retorna a
área desse retângulo. Em seguida, o programa deve
solicitar ao usuário que insira o comprimento e a
largura e imprimir a área calculada.
'''

def calcular_area_retangulo(comprimento: float, largura: float) -> float:
    area = comprimento * largura
    return area

comp = float(input('Digite o comprimento do retangulo: '))
larg = float(input('Digite a largura do retangulo: '))

print(f'A area do retangulo é {calcular_area_retangulo(comp, larg)} m2')