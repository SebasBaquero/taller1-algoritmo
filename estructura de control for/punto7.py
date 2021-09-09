#Busque e imprima la Capiltal de Colombia
archivo= open("paises.txt", "r")
lista= []
for i in archivo:
  lista.append(i)
  e= " ".join(lista)
  if(e == "Colombia: Bogotá \n"):
    break
  lista= []
c= e.index(":")
t= len(e)
lista1= []
for i in range(c, t):
    lista1.append(e[i])
    u= "".join(lista1)
print("La capital de Colombia es "+str(u))
archivo.close()
