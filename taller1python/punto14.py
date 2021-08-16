"""
Entradas
ce-->float-->Consumo de energía en kilowatts
pk-->float-->Precio por kilowatt
Salidas
vp-->float-->Valor a pagar
"""
ce=float(input("Escriba el consumo de energia en Kilowatt: "))
pk=float(input("Escriba el precio por Kilowatt: "))

vp=ce*pk
print("El valor a pagar es de: "+str(vp))
