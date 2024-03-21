def bem_vindo():
    print('Bem vindo')


def boa_tarde(pessoa: str) -> str:
    nome = pessoa
    return f'Boa Tarde {nome}'



bem_vindo()
nome = 'Leonardo'
print(boa_tarde(nome))

