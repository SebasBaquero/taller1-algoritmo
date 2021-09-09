#Cuente e Imprima las ciudades que su pais inicie con la letra E
archivo= open("paises.txt", "r")
lista= []
paises= []
for i in archivo:
  e= i.index(":")
  for r in range(0, e):
    lista.append(i[r])
  e= "".join(lista)
  paises.append(e)
  lista= []
for i in paises:
  if(i[0] == "E"):
    print(i)
    lista.append(i)
print(len(lista))
archivo.close()
