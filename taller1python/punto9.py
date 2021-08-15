"""
Entradas
Horas trabajo-->float-->horast
Pago hora-->float-->pagoh
Salidas
Pago por horas-->float-->p=horast*pagoh
Descuento por los impuestos-->float-->caja=p*0.20 y des=p-caja
"""
horast=float(input("Escriba las horas que ha trabajado: "))
pagoh=float(input("Escriba el pago por hora: "))
p=horast*pagoh
caja=p*0.20 
des=p-caja
print("El pago sera de: ", des)
 
