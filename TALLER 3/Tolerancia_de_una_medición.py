"""
Cree las funciones necesarias para tolerancia de una medición. Debe reutilizar una función de
valor absoluto que recibe un real y devuelve su distancia al cero. Los extremos de tolerancia se aceptan.
La función de aceptación utiliza el retorno de valor absoluto. El escenario consulta dos mediciones por
separado. Contratos en orden de parámetros: Valor absoluto: recibe real finito y devuelve real no
negativo. Aceptación: recibe medición y objetivo reales, tolerancia real no negativa y devuelve lógico.
"""
def valor_absoluto(numero):
    if numero >= 0:
        return numero
    else:
        return -numero

def aceptacion(medicion, objetivo, tolerancia):
    error = valor_absoluto(medicion - objetivo)
    if error <= tolerancia:
        return True
    else:
        return False

# La terminal te pedirá los datos cuando corras el programa:
objetivo_val = float(input("Ingrese el objetivo: "))
tolerancia_val = float(input("Ingrese la tolerancia: "))

medicion_1 = float(input("Ingrese la medición 1: "))
medicion_2 = float(input("Ingrese la medición 2: "))

r1 = aceptacion(medicion_1, objetivo_val, tolerancia_val)
r2 = aceptacion(medicion_2, objetivo_val, tolerancia_val)

print("Aceptables:", r1, ";", r2)