"""
Entradas
Consumo de luz electrica anterior-->int-->lea
Consumo de luz entrica actual-->int-->le
Salidas
Cantidad a pagar-->int-->cp
"""
lea=int(input("Escriba su consumo de luz electrica anterior: "))
le=int(input("Escriba su consumo de luz electrica actual: "))
c=le-lea
if (c<=100):
    cp=c*4600
elif (c>=101 and c<=300):
    cp=c*80000
elif (c>=301 and c<=500):
    cp=c*100000
elif (c>=501):
    cp=c*120000
print("Debe pagar un monto de: ",cp, "COP/Khw")
