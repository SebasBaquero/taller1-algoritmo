"""
Entradas
Longitud del triangulo-->float-->a,b,c
Salida
sempiperimetro-->float-->d=(a+b+c)/2
Area-->float-->a=math.sqrt(d*(d-a)*(d-b)*(d-c))
"""
import math
print("Escriba las longitudes de los lados del triangulo: ")
a, b, c = map(float, input().split())
d=(a+b+c)/2
area=math.sqrt(d*(d-a)*(d-b)*(d-c))
print("El area del triangulo es de: ", area)
