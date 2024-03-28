'''
ATIVIDADE PRÁTICA 1
Crie um programa que solicita ao usuário que insira três
notas e, em seguida, calcule a média dessas notas
usando uma função. A função deve receber as três
notas como argumentos e retornar a média. Por fim, o
programa deve imprimir a média calculada.
'''
from math import trunc


def calcula_media(n1:int, n2:int, n3:int) -> int:
    media = (n1+n2+n3) / 3
    return media # type: ignore


num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))

print(trunc(calcula_media(num1,num2,num3)))