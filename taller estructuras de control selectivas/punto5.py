"""
Entradas
SalarioBruto-->int-->sb
Ventas del departamento 1-->int-->v1
Ventas del departamento 2-->int-->v2
Ventas del departamento 3-->int-->v3
"""
sb=int(input("Escriba el salario bruto: $"))
v1=int(input("Escriba las ventas del departamento 1: "))
v2=int(input("Escriba las ventas del departamento 2: "))
v3=int(input("Escriba las ventas del departamento 3: "))
suma=v1+v2+v3
f=(33*suma)/100
if (v1>f):
    print("El salario de los trabajadores del departamento 1 es de $"+str(sb+(sb*0.2)))
else:
    print("El salario de los trabajadores del departamento 1 es de $"+str(sb))
if (v2>f):
    print("El salario de los trabajadores del departamento 2 es de $"+str(sb+(sb*0.2)))
else:
    print("El salario de los trabajadores del departamento 2 es de $"+str(sb))
if (v3>f):
    print("El salario de los trabajadores del departamento 3 es de $"+str(sb+(sb*0.2)))
else:
    print("El salario de los trabajadores del departamento 3 es de $"+str(sb))
