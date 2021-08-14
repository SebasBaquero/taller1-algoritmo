a, b, c= map(float, input().split())
pi= 3.14159
triangle= (c*a)/2
circle= pi * pow(c,2)
trapezium= ((a+b) / 2)*c
square= pow(b,2)
rectangle= a*b
print("TRIANGULO: %.3f" %triangle)
print("CIRCULO: %.3f" %circle)
print("TRAPEZIO: %.3f" %trapezium)
print("QUADRADO: %.3f" %square)
print("RETANGULO: %.3f" %rectangle)
