"""
entradas
valorA-->float-->a
valorB-->float-->b
valorC-->float-->c
salidas
valorX1-->str-->x1
valorX2-->str-->x2
"""
a= float(input("Escriba el valor de A: "))
b= float(input("Escriba el valor de B: "))
c= float(input("Escriba el valor de C: "))
d= b**2-4*a*c
if(d==0):
  x1 = x2 = -b/(2*a)
  print("El valor de x1 es "+str(x1)+" y el valor de x2 es "+str(x2))
elif(d>0):
  x1= (-b+(b**2-4*a*c)**0.5)/(2*a)
  x2= (-b-(b**2-4*a*c)**0.5)/(2*a)
  print("El valor de x1 es "+str(x1)+" y el valor de x2 es "+str(x2))
else:
  print("No tiene solución en los Reales")
