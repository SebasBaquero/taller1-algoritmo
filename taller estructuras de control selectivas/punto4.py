"""
entadas
numeroPiezas->int->np
costoPiezas->int->cp
salidas
inversion->str->inv
prestamo->str->pre
credito->str->credito
intereses->str->intereses
"""
np=int(input("Escriba el numero de piezas por comprar: "))
cp=int(input("Escriba el precio de la pieza: $"))
a=np*cp
if a>5000000:
 inv=a*0.55
 pre=a*0.30
 credito=a*0.15
else: 
 inv=a*0.70
 pre=0 
 credito=a*0.30
intereses=credito*0.20
print("La inversion de la empresa es de: "+str (inv))
print("El prestamo del banco es por "+str (pre))
print("El credito es de $"+ str (credito))
print("El credito es de $" + str(credito))
print("Los intereses del credito son de $" + str(intereses))
