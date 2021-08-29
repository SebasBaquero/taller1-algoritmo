"""
Entradas
valores de los productos-->datos
Salidas
Alcool-->alcool
Gasolina-->gas
Diesel-->diesel
"""
alcool = 0
gas = 0
diesel = 0

while True:
    datos= int(input())
    if(datos==4):
      break
    elif (datos == 1):
        alcool = alcool+ 1
    
    elif (datos == 2):
        gas = gas+ 1
    
    elif (datos == 3):
        diesel = diesel+ 1
    
print("MUITO OBRIGADO")
print("Alcool:", alcool)
print("Gasolina:",gas)
print("Diesel:", diesel)
