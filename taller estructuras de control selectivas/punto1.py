capital= float(input("Ingrese el capital a invertir: "))
tasa= float(input("Ingrese la tasa de interes: "))
interes= tasa*capital/100
print("Interes $", interes)
if interes > 100000:
  print("los intereses superan los $100.000 ")
print("el saldo final ya con los intereses es: $", capital+interes)
