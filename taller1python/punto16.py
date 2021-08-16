"""
Entradas
cg-->float-->Cantidad de galones
Salidas
p-->float-->Precio
"""
cg=float(input("Escriba la cantidad de galones: "))
p=(cg*3.785)*50000
print("El valor a pagar es de: "+str(p))
