# Suponha que você está gerenciando uma competição esportiva e tem
# uma lista de tuplas representando os resultados das equipes em
# diferentes modalidades. Cada tupla contém o nome da equipe, seguido
# por uma lista de pontuações obtidas em cada rodada da competição.

# 1.Calcule a média das pontuações de cada equipe e armazene esses
# valores em uma nova lista chamada medias.
# 2.Ordene a lista medias em ordem decrescente.
# 3.Crie uma nova lista chamada classificacao que contém tuplas, onde
# cada tupla contém o nome da equipe e sua média de pontuações.
# 4.Exiba na tela a classificação final das equipes, mostrando o nome da
# equipe e sua média, da equipe com a pontuação mais alta para a
# mais baixa.

tupla_competição = (('Equipe Raiz', [5, 10, 7, 9, 8]), ('Equipe Bola de Ouro', [5, 9, 10, 5, 4]), 
                    ('Equipe Fedora', [10, 8, 4, 9, 10]), ('Equipe Red Hat', [3, 10, 10, 10, 4]),
                    ('Equipe Bala de Prata', [2, 4, 10, 10, 3]),('Equipe Espelho', [10, 10, 10, 9, 8]))
lista_medias = []
for equipe, media in tupla_competição:
    for nota in range(0, len(media)):
        print(media[nota], end=' ')
