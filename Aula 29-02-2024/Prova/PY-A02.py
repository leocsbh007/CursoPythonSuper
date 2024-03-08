# [PY-A02] Faça um programa que solicite ao usuário que digite 10 valores para preencher uma lista. 
# Em seguida, o programa deve separar os números pares e ímpares em listas diferentes. 
# Por fim, exiba na tela os números pares, os números ímpares em uma tupla, a quantidade de números pares e ímpares presentes na lista,
# e a soma de todos os números pares e ímpares, respectivamente.

count = 0
numeros = []
num_pares = []
num_impares = []

while count < 5:
    numeros.append(int(input("Digite um numero: ")))
    count = count + 1
else:
    for numero in numeros:
        #Verifica se o numeros é par ou impar
        if numero % 2 == 0:
            num_pares.append(numero)
            
        else:
            num_impares.append(numero)
    
    # Cria uma tupla com a lista de numeros pares, lista de numeros impares, quantidade de numeros pares, quantidade de numeros impares
    # soma dos numeros pares e soma dos numeros impares
    tupla_resultado =( num_pares , num_impares , len(num_pares) , len(num_impares), sum(num_pares),  sum(num_impares))
  
    print(tupla_resultado, num_pares.length())