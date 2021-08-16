"""
entrada
precio pago contado-->int-->pc
precio cuotas-->int-->pp
salidas
recargo-->str-->a
"""
pc=int(input("Escriba el precio del producto con pago al contado: "))
pp = int(input("Escriba el precio del producto con pago a cuotas: "))
b=(pp-pc)
a=(b/pp)*100
print("El recargo es de: "+ str (a),"%")
