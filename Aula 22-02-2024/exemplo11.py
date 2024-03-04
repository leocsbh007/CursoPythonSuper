# Numeros primos

numero = int(input("Entre com um numero: "))
contador = 2
while contador < numero:
    if numero % contador == 0:        
        break
    contador = contador + 1
    
print("primo" if contador >= 3 else "não primo")