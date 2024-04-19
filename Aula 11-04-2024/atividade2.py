'''
ATIVIDADE PRÁTICA 2

Crie um dicionário com informações de produtos,
incluindo nome, preço e quantidade em estoque.

Implemente funções para adicionar, remover e atualizar

produtos no dicionário.

'''
def adicionar_produto(nome: str, preco: float, quantidade: int) -> dict:
    produtos["nome"] = nome
    produtos["preco"] = preco
    produtos["quantidade"] = quantidade
    return produtos

def remover_produto(nome: str, produtos: dict) -> bool:
    if len(produtos) == 0:        
        return False
    elif produtos["nome"] == nome:
        produtos.clear()        
        return True
    
def atualizar_produto(produtos: dict, nome: str, preco: float, quantidade: int) -> dict:
    if len(produtos) == 0:                
        return produtos
    else:        
        produtos["nome"] = nome
        produtos["preco"] = preco
        produtos["quantidade"] = quantidade
        return produtos


produtos = {}

nome = "Bola"
preco = 12.9
quantidade = 10


print(adicionar_produto(nome, preco, quantidade))

nome = "Bandeira"
preco = 12.9
quantidade = 20

print(atualizar_produto(produtos, nome, preco, quantidade))
print(remover_produto(nome, produtos))
print(produtos)



