#Imprima la posicion del Pais de Mexico
archivo= open("paises.txt", "r")
c=0
posicion=[]
for i in archivo:
  posicion.append(i)
  a=" ".join(posicion)
  c=c+1 
  if(a=="México\n"):
    break
  posicion=[]   
print("Mexico se encuentra en la posición: ",(c))
archivo.close()
