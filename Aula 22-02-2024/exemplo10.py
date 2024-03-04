# Numeros primos

numero = int(input("Entre com um numero: "))
contador = True
for i in range(2, numero):
    if numero % i == 0:
        contador = False
        break
print("primo" if contador == True else "não primo")