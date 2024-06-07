from PY_A11_Elevador import Elevador


# Testes da Classe
# totalCapacidade:int, atualCapacidade:int, totalAndar:int, atualAndar:int
elevador = Elevador(10, 6, 10, 9)
print(elevador.entrar())
print(elevador.totalCapacidade, elevador.atualCapacidade, elevador.totalAndar, elevador.atualAndar)

print(elevador.subir())
print(elevador.totalCapacidade, elevador.atualCapacidade, elevador.totalAndar, elevador.atualAndar)
print(elevador.subir())
print(elevador.totalCapacidade, elevador.atualCapacidade, elevador.totalAndar, elevador.atualAndar)

for i in range(11):
    print(elevador.sair())
    print(elevador.totalCapacidade, elevador.atualCapacidade, elevador.totalAndar, elevador.atualAndar)


for i in range(11):
    print(elevador.descer())
    print(elevador.totalCapacidade, elevador.atualCapacidade, elevador.totalAndar, elevador.atualAndar)

# print(elevador.subir())
# print(elevador.descer())