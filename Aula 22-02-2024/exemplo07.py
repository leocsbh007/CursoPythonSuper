# Ler um plavra do teclado e exibir de tras pra frente

palavra = input("Digite uma palvra: ")
indice = 1

while indice <= len(palavra):
    print(palavra[-indice])
    indice += 1