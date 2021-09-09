#Imprima todos los paises y capitales, cuyo inicio sea con la letra U
archivo = open("paises.txt", "r")
lista= []
paises= []
for i in archivo:
  a= i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista1)
  paises.append(a)
  lista= []
for i in paises:
  if(i[0]=="U"):
    print(i)
print()
archivo = open("paises.txt", "r")
lista1=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista1.append(i[r])
  a="".join(lista2)
  ciudad.append(a)
  lista1= []
for i in ciudad:
  if(i[0]=="U"):
    print(i)
archivo.close()
