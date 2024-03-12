# ATIVIDADE PRÁTICA 7

# Escreva um programa que receba duas listas e calcule a união dos elementos únicos dessas listas, usando conjuntos.

lista_1 = [1, 2 ,3 ,4 ,5, 6]

lista_2 = [10, 1, 2, 3, 29]

conjunto = set(lista_1)

conjunto = conjunto.union(lista_2)

        
print(conjunto)