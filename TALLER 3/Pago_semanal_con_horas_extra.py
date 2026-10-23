"""
Cree una función para pago semanal con horas extra. Es un modelo ficticio: las primeras 40 horas
se pagan a la tarifa ordinaria; solo las horas que exceden 40 se pagan a 1,5 veces esa tarifa. Llame para
dos personas y sume los retornos, sin redondearlos antes de sumar. Contrato: Pago semanal con horas
extra: recibe horas semanales reales no negativas y tarifa real no negativa en pesos por hora y devuelve
el pago real semanal en pesos.
"""
def pago_semanal(horas, tarifa):
    if horas <= 40:
        pago = horas * tarifa
    else:
        pago = (40 * tarifa) + ((horas - 40) * tarifa * 1.5)
    return pago

# La terminal te pedirá los datos cuando corras el programa:
print("--- Datos de la Persona 1 ---")
horas_1 = float(input("Ingrese horas de la persona 1: "))
tarifa_1 = float(input("Ingrese tarifa de la persona 1: "))

print("--- Datos de la Persona 2 ---")
horas_2 = float(input("Ingrese horas de la persona 2: "))
tarifa_2 = float(input("Ingrese tarifa de la persona 2: "))

p1 = pago_semanal(horas_1, tarifa_1)
p2 = pago_semanal(horas_2, tarifa_2)
total = p1 + p2

print("Pagos:", int(p1), "y", int(p2), "; total:", int(total))