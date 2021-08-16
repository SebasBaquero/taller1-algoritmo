"""
entrada
valor_prestamo-->float-->a
valor_intereses-->float-->b
tiempo-->float-->t
salida
intereses-->str-->inte
"""
a=float(input ("Escriba el valor del pestramo: " ))
b=float(input ("Escriba el valor de los intereses: "))
t=4
inte=(a*t*b)/100
print("el interes en cuatro años es del " +str (inte))
