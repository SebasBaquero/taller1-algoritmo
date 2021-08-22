"""
entrada
sueldo-->int-->sueldo
salidas
nuevoSueldo-->str-->aumento
"""
sueldo=int(input("Escriba su sueldo $"))
if sueldo<900000:
 aumento=sueldo+(sueldo*0.15)
else:
 aumento=sueldo+(sueldo*0.12)
print("Su nuevo sueldo es de $"+str (aumento))
