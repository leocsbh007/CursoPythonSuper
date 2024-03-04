# Ler um plavra do teclado e exibir de tras pra frente

palavra = input("Digite uma palavra: ")
tam_palavra = len(palavra)
for indice in range (1, tam_palavra+1):
    letra = palavra[-indice] 
    print(letra)