# [PY-A05] Suponha que você tenha a seguinte função em Python:
# Se você chamar a função da seguinte maneira: ‘minha_funcao (1,2,3,nome=”Alice”, idade=25), qual será a saída?

def minha_funcao(*args, **kwargs):

    for arg in args:

        print(arg)

    for key, value in kwargs.items():

        print(key, value)


minha_funcao (1,2,3,nome='Alice', idade=25)
