def somar_numeros(*args):
    soma = 0
    for numero in args:
        soma += numero
    return soma

soma1 = somar_numeros(1)
soma2 = somar_numeros(2,8,10,9)
print(soma1)
print(soma2)