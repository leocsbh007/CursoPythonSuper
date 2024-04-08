'''
[PY-A05] Considere o seguinte trecho de código: 

numeros = [1, 2, 3, 4, 5]



resultado = list(map(lambda x: x ** 2 if x % 2 == 0 else x ** 3, numeros))



'''

numeros = [1, 2, 3, 4, 5]
resultado = list(map(lambda x: x ** 2 if x % 2 == 0 else x ** 3, numeros))

print(resultado)