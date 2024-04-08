'''
ATIVIDADE PRÁTICA 2

Crie um módulo chamado manipulacao_strings que
contenha funções para realizar operações com strings,
como inverter uma string, contar o número de palavras
em uma string e verificar se uma string é um
palíndromo (lê-se igual de trás para frente). Crie
um programa principal que importe o módulo e use
essas funções com strings fornecidas pelo usuário.
'''

from manipulacao_strings import *

nome = 'arara'
i = 0
tam = len(nome)-2
palin = True
print(i, tam)

for palavra in nome:
    if palavra[i] != palavra[tam]:
        palin = False
        break
    else: 
        i =+ 1
        tam =-1
        palin = True
        
if palin == True:
    print('Palindromo')
else:
    print('Não é Palindromo')
    
    
    


# print(contar_palavras(nome))

# print(len(nome))
# print(len(nome.split()))

