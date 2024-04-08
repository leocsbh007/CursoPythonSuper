def calcular_area_e_perimetro(lado_quadrado:float) -> tuple[float, float]:
    area = lado_quadrado ** 2
    perimetro = lado_quadrado * 4 
    return area, perimetro


lado = 2

area, perimetro = calcular_area_e_perimetro(lado)

print(f'Area {area}')
print(f'Perimetro {perimetro}')