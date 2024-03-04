# 1 1 2 3 5 8 13 21 34 55 ... n
# sequencia de fibonnacci
numero = 10
ultimo = 1
penultimo = 1

if numero == 1 or numero == 2:
    print(1)
else:
    contador = 3
    while contador <= numero:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        contador += 1
        
    print(termo)