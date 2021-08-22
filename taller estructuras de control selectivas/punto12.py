"""
Entradas
MontoDinero-->int-->a
"""
md=int(input("Ingrese monto de dinero en COP: $"))

billetes_de_100000=(md-md%100000)/100000
md=md%100000
billetes_de_50000=(md-md%50000)/50000
md=md%50000
billetes_de_20000=(md-md%20000)/20000
md=md%20000
billetes_de_10000=(md-md%10000)/10000
md=md%10000
billetes_de_5000=(md-md%5000)/5000
md=md%5000
billetes_de_2000=(md-md%2000)/2000
md=md%2000
billetes_de_1000=(md-md%1000)/1000
md=md%1000
monedas_de_500=(md-md%500)/500
md=md%500
monedas_de_200=(md-md%200)/200
md=md%200
monedas_de_100=(md-md%100)/100
md=md%100
monedas_de_50=(md-md%50)/50
md=md%50
print("La Cantidad de billetes de 100000 es de: "+str(billetes_de_100000), "COP")
print("La Cantidad de billetes de 50000 es de: "+str(billetes_de_50000), "COP")
print("La Cantidad de billetes de 20000 es de: "+str(billetes_de_20000), "COP")
print("La Cantidad de billetes de 10000 es de: "+str(billetes_de_10000), "COP")
print("La Cantidad de billetes de 5000 es de: "+str(billetes_de_5000), "COP")
print("La Cantidad de billetes de 2000 es de: "+str(billetes_de_2000), "COP")
print("La Cantidad de billetes de 1000 es de: "+str(billetes_de_1000), "COP")
print("La Cantidad de monedas de 500 es de: "+str(monedas_de_500), "COP")
print("La Cantidad de monedas de 200 es de: "+str(monedas_de_200), "COP")
print("La Cantidad de monedas de 100 es de: "+str(monedas_de_100), "COP")
print("La Cantidad de monedas de 50 es de: "+str(monedas_de_50), "COP")
