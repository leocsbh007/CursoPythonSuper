'''
ATIVIDADE PRÁTICA 5

Dado um dicionário que representa as vendas de
produtos, encontre o produto mais vendido (ou os
produtos mais vendidos, se houver um empate).
'''

produtos = {
    "Codigo 1": {"nome": "Bola", "preco": 12.00, "qtde_vendas": 10},
    "Codigo 2": {"nome": "Carrinho", "preco": 9.00, "qtde_vendas": 7},
    "Codigo 3": {"nome": "Pula Pula", "preco": 22.00, "qtde_vendas": 2},
    "Codigo 4": {"nome": "Jogo de Botão", "preco": 19.00, "qtde_vendas": 10},
            }

# print(produtos["Codigo 4"]["qtde_vendas"])
# maximo = max(produtos)
# print(maximo)
maior = 0
i = 0
for codigo, produto in produtos.items():
    print("="*80)
    # print(codigo, produto)    
    # print(produto["qtde_vendas"])

    # print(produto)
    for chave in produto:
        print(type(chave))  
    

