# ATIVIDADE PRÁTICA 11

# Escreva um programa que recebe um dicionário e uma
# lista de chaves como entrada e verifica se todas as
# chaves da lista existem no dicionário. A função deve
# retornar True se todas as chaves existirem e False caso
# contrário.

dicionario_usuario = {
    'Nome' : 'Fulano',
    'idade' : 18,
    'sexo' : 'masculino',
    'salario' : 1500.37,
}
lista_chave = ['Peso', 'idade', 'sexo', 'salario']

existe = True

for chave in lista_chave:
    if chave in dicionario_usuario:
        existe = True
    else:
        existe = False
        break

if existe:
    print("Todas as chaves estão no dicionario")  
else:  
    print("Não tem todas as chaves no dicionario")  