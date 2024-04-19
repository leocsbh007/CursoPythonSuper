'''
ATIVIDADE PRÁTICA 3

Crie um conjunto com nomes de cores. Implemente uma
função que retorne as cores que têm mais de quatro letras.

'''
def contar_letras(cores: set) -> list:
    cor_maior_4 = []
    for cor in cores:
        # print(cor)
        if (len(cor) > 4):
            cor_maior_4.append(cor)
    return cor_maior_4



cores = {"Amarelo", "Verde", "Azul", "Preto", "Anil", "Branco", "Roxo"}

print(contar_letras(cores))
