#Cuente e Imprima cuantos paises que hay en el archivo
archivo = open("paises.txt", "r")
b= 0
lista= []
for i in archivo:
  lista.append(i)
  a= " ".join(lista)
  b= b+1
print(len(lista))
archivo.close()
