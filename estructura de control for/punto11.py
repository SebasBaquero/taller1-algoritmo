#Agregue un país que no esté en la lista
archivo= open("paises.txt", "r")
c= 0
lista= []
for i in archivo:
  lista.append(i)
  a= " ".join(lista)
  c= c+1 
  if(a=="Paises\n"):
    break
b= a.index(":")
lista1= [] 
for i in range(0,len(a)):
      lista1.append(a[i])
lista1.insert(0,"Wakanda: Forever\n")
u="".join(lista1)
print(u)
archivo.close()
