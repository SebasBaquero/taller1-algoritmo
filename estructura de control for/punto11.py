#Agregue un país que no esté en la lista
archivo= open("paises.txt", "r")
lista=[]
lista.append("Vegetta\n")
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a= "".join(pais)
  print(a)
  lista= []
archivo.close()
