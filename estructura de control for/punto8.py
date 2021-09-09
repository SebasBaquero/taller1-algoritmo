#imprima la posicion del pais de Uganda
archivo= open("paises.txt", "r")
c= 0
lista= []
for i in archivo:
  lista.append(i)
  uganda= " ".join(lista)
  c= c+1
  if(uganda == "Uganda: Kampala \n"):
    break
  lista= []
print(c)
archivo.close()
