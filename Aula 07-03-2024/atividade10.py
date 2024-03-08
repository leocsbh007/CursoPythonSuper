# ATIVIDADE PRÁTICA 10

# Desenvolva um programa que recebe um dicionário, uma
# chave e um valor como entrada e adiciona a chave e o
# valor ao dicionário, atualizando o valor se a chave já
# existir.

pessoas = {}
controle = True

while controle:   
    chave = input("Entre com a Chave: ")    
    if chave == "0":
        controle = False          
    elif chave in pessoas:        
        valor = input("Entre com o Valor: ")
        pessoas[chave] = valor
    else:
        valor = input("Entre com o Valor: ")
        #pessoas.update({chave: valor})        
        pessoas[chave] = valor

else:
    print(pessoas)
    
