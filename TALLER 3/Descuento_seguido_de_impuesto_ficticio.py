"""
Cree las funciones necesarias para descuento seguido de impuesto ficticio. El descuento se calcula
sobre la base. El impuesto se calcula sobre el subtotal ya descontado, no sobre la base original. Son
reglas ficticias, no normas tributarias. El escenario pasa el retorno del descuento a la función de
impuesto y muestra subtotal y total. Contratos en orden de parámetros: Subtotal descontado: recibe
base real no negativa en pesos, descuento real de 0 a 100 por ciento y devuelve real no negativo en
pesos. Total con impuesto: recibe subtotal real no negativo en pesos, impuesto real no negativo por
ciento y devuelve real no negativo en pesos.
"""
# 5. Descuento seguido de impuesto ficticio

def subtotal_descontado(base, descuento):
    return base * (1 - descuento / 100)

def total_con_impuesto(subtotal, impuesto):
    return subtotal * (1 + impuesto / 100)

# La terminal te pedirá los datos cuando corras el programa:
base_valor = float(input("Ingrese la base: "))
descuento_valor = float(input("Ingrese el porcentaje de descuento: "))
impuesto_valor = float(input("Ingrese el porcentaje de impuesto: "))

sub = subtotal_descontado(base_valor, descuento_valor)
tot = total_con_impuesto(sub, impuesto_valor)

print("Subtotal:", int(sub), "; total:", int(tot), "pesos")