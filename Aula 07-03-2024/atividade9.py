# ATIVIDADE PRÁTICA 9
# Escreva um programa que percorra as chaves e valores
# de um dicionário separadamente e os exiba.

pessoas1 = {
    'nome' : 'Leonardo',
    'idade' : 45,    
}

pessoas2 = {
    'nome' : 'José',
    'idade' : 29,    
}

lista_pessoas = [pessoas1, pessoas2]
for elemento in lista_pessoas:
    print(elemento['nome'])
    print(elemento['idade'])
    print("-"*10)
    
