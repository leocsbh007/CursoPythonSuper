from veiculo import *

car = Carro("Amarelo", "Fox", "Carro")
bic = Bicicleta("Verde", "Monareta", "Bicicleta")

car.mostra_cor_modelo()
bic.mostra_cor_modelo()
car.alterar_cor("Cinza")
car.mostra_cor_modelo()
bic.alterar_modelo("Caloi")
bic.mostra_cor_modelo()