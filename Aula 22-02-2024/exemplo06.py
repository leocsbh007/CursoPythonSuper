# Ler um plavra do teclado e exibir de tras pra frente

palavra = input("Digite uma palvra: ")
invertida = ""

for letra in palavra:
    invertida = letra + invertida
    
print(invertida)