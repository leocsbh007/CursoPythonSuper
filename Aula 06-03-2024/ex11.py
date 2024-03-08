pessoas = {
    1: {
        "nome": "Caio",
        "idade": 12
    },
    2: {
        "nome": "Julia",
        "idade": 24
    },
    3: {
        "nome": "Paulo",
        "idade": 26
    }
}

for chave1 in pessoas:
    for chave2 in pessoas[chave1]:
        print(chave2)

