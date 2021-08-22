"""
Entradas:
valorP-->int-->P
valorQ-->int-->Q
Salidas:
Expresion-->str-->ex
"""
P = int(input("Escriba el valor de P: "))
Q = int(input("Escriba el valor de Q: "))
a = (P**3)+(Q**4)-(2*P**2)
if(a < 680):
    print(str(P),"y "+str(Q),"no satisfacen la expresión")
elif(a > 680):
    print(str(P),"y "+str(Q),"satisfacen la expresión")
