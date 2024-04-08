import math
from random import *
import time

num = 9
raiz = math.sqrt(num)
print(raiz)
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
lista = ['pedra', 'papel', 'tesoura']


escolha_pc = choice(lista)
print(escolha_pc)