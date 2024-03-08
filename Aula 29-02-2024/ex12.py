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

media_pontos = 0
count = 0
lista_classificação = []
lista_classificação_decrescente = []

# Varre a Tupla para buscar as listas de pontos de cada equipe
for equipe, media in tupla_competição:   
    # Calcula a media de pontuação de cada equipe e insere em um lista 
    for nota in range(0, len(media)):        
        #print(media[nota], end=' ')
        media_pontos = media_pontos + media[nota]
        count = count + 1
        if count == len(media):
            count = 0
            media_pontos = media_pontos/len(media)            
            #lista_medias.append(round(media_pontos,2))
    # Cria uma lista com o time e sua media de pontos      
    lista_classificação.append((round(media_pontos,2), equipe))

# Ordena uma lista usando o primeiro elemento de cada Tupla de forma decrescente   
lista_classificação_decrescente = sorted(lista_classificação, reverse=True)
# Imprime A equipe e sua nota media
for equipe in lista_classificação_decrescente:
    print(equipe[1]," - media de pontos: ", equipe[0])

