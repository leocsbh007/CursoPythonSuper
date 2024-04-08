'''
[PY-A05] Considere uma lista de números inteiros 
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Utilizando as funções map(),filter() e reduce(), escreva um código que execute as seguintes operações:


Função map() para obter uma nova lista com o quadrado de cada número da lista numeros

Função filter() para obter uma nova lista com números pares da lista numeros

Função reduce()  para obter a soma de todos os números da lista numeros

Qual o resultado obtido após a execução das operações acima?
'''

from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Obtendo o quadrado de cada numero da Lista
numeros_quadrados = list(map(lambda x: x * x, numeros))
# Obtendo apenas os numeros pares da Lista
numeros_pares = list(filter(lambda x : x % 2 == 0, numeros))
# Obtendo a soma dos numeros da Lista
numeros_somados = reduce(lambda x, soma: x + soma, numeros)

print(f'O quadrado de cada numero da lista: {numeros_quadrados}')
print(f'Mostra apenas os numeros pares: {numeros_pares}')
print(f'A soma de todos os numeros da lista: {numeros_somados}')