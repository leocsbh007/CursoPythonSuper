'''
ATIVIDADE PRÁTICA 5
Crie uma função que aceita uma lista de números e use
a função filter para retornar uma nova lista contendo
apenas os números pares da lista de entrada.
'''


def numeros_pares(num):
    temp = 0
    for par in num:
        temp = par % 2
    return temp


numeros = [1, 2, 4, 10, 9]
pares = list(filter(numeros_pares(numeros), numeros))

print(pares)
