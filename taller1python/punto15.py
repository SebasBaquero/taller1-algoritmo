"""
Entradas
vp-->float-->precio de venta al publico
fp-->float-->precio final pagado
Salidas
df-->float-->Descuento final
"""
vp=float(input("Escriba el precio de venta al publico: "))
fp=float(input("Escriba el precio final pagado: "))

a=fp/vp
df=(1-a)*100
print("El descuento final es de "+str("{:.2f}".format(df)+"%"))
