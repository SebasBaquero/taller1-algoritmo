"""
Entradas
Categoría-->int-->a
SalarioBruto-->int-->sb
Salidas
salarioAumento-->str-->c
"""
a=int(input("Escriba la categoría: "))
sb=int(input("Escriba el salario bruto: $"))

if (a==1):
    c=("El salario bruto es de: $"+str(sb+(sb*0.1)))
elif (a==2):
    c= ("El salario bruto es de: $"+str(sb+(sb*0.15)))
elif (a==3):
    c= ("El salario bruto es de: $"+str(sb+(sb*0.2)))
elif (a==4):
    c= ("El salario bruto es de: $"+str(sb+(sb*0.40)))
elif (a==5):
    c= ("El salario bruto es de: $"+str(sb+(sb*0.6)))
else:
    c=("Categoria inexistente")
print(c)
