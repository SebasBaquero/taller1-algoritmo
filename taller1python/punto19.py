"""
entrada
lote-->int-->a
venta-->float-->b
docenas-->int-->c
salida
descuento-->float-->e
"""
a = int(input("Escriba el numero de lotes: "))
b= int(input("Escriba el valor total de ventas: "))
c= int(input("Escriba la cantidad de docenas: "))
d = (b*c)-a
e = 100-((a/d)*100)
print("La ganancia es de: " + str(e), "%")
