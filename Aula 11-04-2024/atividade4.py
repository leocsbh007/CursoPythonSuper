'''
ATIVIDADE PRÁTICA 4

Crie uma função que receba uma lista de strings e
retorne uma nova lista contendo apenas as strings

palíndromos.
'''
def lista_palindromos(nomes: list) -> list:
    nome_reverso = ""
    palindromos=[]
    for nome in nomes:
        nome_reverso = nome[::-1]
        if nome == nome_reverso:     
            palindromos.append(nome)            
    return palindromos

    
    
nomes = ["bola", "arara", "bicicleta", "ovo", "ixi", "cadeira"]
    
print(lista_palindromos(nomes))

# print(nome)
# print(nome_reverso)

