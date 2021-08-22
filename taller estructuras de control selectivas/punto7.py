Entradas:
kmRecorridos-->float-->kr
Salidas:
precio-->float-->precio
"""
kr = float(input("escriba la distancia recorrida en Km: "))
if(kr <= 300 and kr > 0):
  precio = 50000
  print("El valor a pagar es de $"+str(precio))
elif(kr > 300 and kr <= 1000):
  precio = (70000+((kr-300)*30000))
  print("El valor a pagar es de $"+str(precio))
if(kr > 1000):
  precio = (150000+((kr-1000)*9000))
  print("El valor a pagar es de $"+str(precio))
