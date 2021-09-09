#Busque e Imprima la ciudad de Singapur
archivo= open("paises.txt", "r")
lista= []
for i in archivo:
  lista.append(i)
  a= " ".join(lista)
  if (a== "Singapur: Singapur \n"):
    break
  lista= []
c= a.index(":")
lista1= []
for i in range(0, c):
    lista1.append(a[i])
    u= "".join(lista1)
print(u)
archivo.close()
