#El alcalde de Antananarivo contrato a algunos alumnos de la Universidad Ean para corregir el archivo de países.txt, ya que la capital de Madagascar NO es rey julien es Antananarivo, espero que el alcalde se vaya contento por su trabajo. Utilice un For para cambiar ese Dato
archivo= open("paises.txt", "r")
lista=[]
for i in archivo:
  lista.append(i)
  a= " ".join(lista)
  if(a=="Madagascar: rey julien\n"):
    break
    for i in archivo:
      lista= i.index(":")
    for r in range(a+2,len(i)):
      lista.append(i[r])
    a= "".join(lista)
    lista.append(a)
    for i in pais:
      if(i=="rey julien"):
        lista.append(i)
        lista.pop(i)
        lista.append("Antananarivo")
    lista= []
    print(lista)
archivo.close()
