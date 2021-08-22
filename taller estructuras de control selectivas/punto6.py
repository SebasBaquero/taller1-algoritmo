"""
Entradas:
VariableA-->int-->a
VariableB-->int-->b
VariableC-->int-->c
VariableD-->int-->d
Salidas:
valor-->str-->v
"""
variables = input("Escriba las variables A,B,C D: ").split()
a, b, c, d = variables
a = int(a)
b = int(b)
c = int(c)
d = int(d)
r = a * 1000
s = b*100
t = c*10
c = d*1
suma = r+s+t+c
v = round(suma, -2)
print("El valor aproximado es: "+str(v))
