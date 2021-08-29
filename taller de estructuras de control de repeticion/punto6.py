"""
Entradas
dividendo-->int-->dividendo
divisor-->int-->divisor
Salidas
Método de las restas sucesivas-->int-->dividendo
"""
dividendo=int(input("Escriba el dividendo: "))
divisor=int(input("Escriba el divisor: "))

while(dividendo>= divisor):
    dividendo=dividendo - divisor
    resultado= dividendo
    print("El método de las restas sucesivas es igual a: "+str(dividendo))
   
