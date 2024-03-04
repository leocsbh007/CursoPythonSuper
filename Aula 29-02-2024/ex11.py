# Crie uma tupla para representar as informações de três
# palestrantes, cada uma contendo o nome, o tema da
# palestra e a instituição à qual estão vinculados.

# Exiba na tela as informações de todos os palestrantes,
# incluindo nome, tema da palestra e instituição.

lista_palestrantes = (('Antonio', 'Acesso a Dados', 'UFMG'),
                      ('José', 'Python Atual', 'Uni-BH'),
                      ('Leo', 'Chat Gpt para Crianças', 'Puc-MG'))

for palestrante, tema, instituicao in lista_palestrantes:
    print(f'Palestrante: {palestrante}')
    print(f'Palestra: {tema}')
    print(f'Instituição: {instituicao}')
    print(20*'=-')

# for ind in range(0, len(lista_palestrantes), 3):
#     print(f'Nome palestrante: {lista_palestrantes[ind]}')
#     print(f'Nome palestra: {lista_palestrantes[ind+1]}')
#     print(f'Nome Instituição: {lista_palestrantes[ind+2]}')
#     print(30*'=-')
