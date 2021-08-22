"""
entrada
a-->int-->a
b-->int-->b
c-->int-->c
salida
respuesta-->str-->resultado
"""
a, b, c, d = map(int, input("Digite los 4 datos: ").split()) 
if d==0 :
 resultado = (a-c)**2
elif d>0 :
    resultado = ((a-b)**3)/d
print("El resultado es: "+str (resultado))
