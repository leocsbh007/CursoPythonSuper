chaves = [1,2,3]
valores = ["um", "dois", "três"]

# Unindo duas listas em um dicionario
dicionario = {chaves[i]: valores[i] for i in range(len(chaves))}
print(dicionario)