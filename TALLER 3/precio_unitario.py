"""
EJERCICIO_2
Cree una función para precio unitario comparable. Dos paquetes pueden tener tamaños distintos;
no compare solo sus precios totales. Llame para dos paquetes y use los retornos para indicar el más
económico por gramo; si coinciden indique igualdad. Contrato: Precio unitario comparable: recibe
precio total real no negativo en pesos y cantidad real positiva en gramos y devuelve el precio real de un
gramo en pesos.
"""
# 2. Precio unitario comparable

def precio_unitario(precio_total, cantidad_gramos):
    return precio_total / cantidad_gramos

# Aquí la terminal te pedirá los datos cuando corras el programa:
precio_1 = float(input("ingrese precio  1: "))
gramos_1 = float(input("Ingrese gramos  1: "))

precio_2 = float(input("Ingrese precio  2: "))
gramos_2 = float(input("Ingrese gramos  2: "))

pu1 = precio_unitario(precio_1, gramos_1)
pu2 = precio_unitario(precio_2, gramos_2)

print("Precios por gramo:", int(pu1), "y", int(pu2))

if pu1 < pu2:
    print("conviene paquete 1")
else:
    if pu2 < pu1:
        print("conviene paquete 2")
    else:
        print("coinciden")