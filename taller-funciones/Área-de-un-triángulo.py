"""
EJERCICIO 1
Cree una función para área de un triángulo por base y altura. La altura es perpendicular a la base.
Use dos llamadas y muestre las dos áreas y su suma, calculada con los retornos. Contrato: Área de un
triángulo por base y altura: recibe base y altura, reales positivos expresados en centímetros y devuelve
el área real en centímetros cuadrados.

"""
def area_de_un_triangulo(base, altura):
    if(base or altura) < 0:
        return None
    return base * altura / 2

base = int(input("digite la base"))
altura = int(input("digite la altura"))

area_1 = area_de_un_triangulo(base, altura)

base_2 = int(input("digite la base"))
altura_2 = int(input("digite la altura"))

area_2 = area_de_un_triangulo(base_2, altura_2)

suma = area_1 + area_2

print("area: ", area_1, "y", area_2, "cm² suma:", suma, "cm²")
