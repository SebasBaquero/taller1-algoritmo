#El alcalde de Antananarivo contrato a algunos alumnos de la Universidad Ean para corregir el archivo de países.txt, ya que la capital de Madagascar NO es rey julien es Antananarivo, espero que el alcalde se vaya contento por su trabajo. Utilice un For para cambiar ese Dato
archivo = open('paises.txt', 'r')
lista= []
for i in archivo:
  lista.append(i)
  a= "".join(lista)
  if(a=="Madagascar: rey julien\n"):
    break
lista1= []
for i in archivo:
  a= i.index(":")
for i in range(0,len(i)):
  lista1.remove("rey julien")
  lista1.insert("Madagascar: Antananarivo")
  print(lista1)
archivo.close()
