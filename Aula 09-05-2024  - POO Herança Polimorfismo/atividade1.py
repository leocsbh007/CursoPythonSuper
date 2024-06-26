from Forma import *

q = Quadrado("quadrado")
r = Retangulo("retangulo")

per_quadrado = q.calcular_perimetro(5)
per_retangulo = r.calcular_perimetro(5, 5)


print(vars(q), per_quadrado)
print(vars(r), per_retangulo)