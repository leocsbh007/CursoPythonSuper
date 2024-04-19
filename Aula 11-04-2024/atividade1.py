'''
ATIVIDADE PRÁTICA 1

Dada uma lista de números, crie uma nova lista contendo

apenas os números pares.
'''

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = []


for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)
    
print(numeros_pares)
    
