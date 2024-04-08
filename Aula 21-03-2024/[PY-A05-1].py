'''
Suponha que você tenha uma lista de palavras:

palavras = ['gato', 'cachorro', 'elefante', 'leão', 'tigre', 'papagaio']

Qual o resultado da função lambda com o filter()?

resultado = list(filter(lambda x: len(x) > 5, palavras))

'''
palavras = ['gato', 'cachorro', 'elefante', 'leão', 'tigre', 'papagaio']
resultado = list(filter(lambda x: len(x) > 5, palavras))

print(resultado)