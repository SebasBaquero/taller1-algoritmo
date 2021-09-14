frutas = open('frutas.txt', 'r')
numeros= open('numeros.txt','r')

lista_frutas=[]#Llenar las lista con los datos del archivo frutas.txt
for i in frutas:
  lista_frutas.append(i)

if __name__ == "__main__":
  print(lista_frutas)


lista_numeros=[]#Llenar las lista con los datos del archivo numeros.txt

for i in numeros:
  lista_numeros.append(i) 

if __name__ == "__main__":
  print(lista_numeros)

#Realizar una funcion que elimine un caracter de todos los elementos de la lista
"""
Entradas:
lista-->list-->lista
elementos-->str-->elemento

Salidas:
lista-->list-->lista
"""
def eliminar_un_caracter_de_toda_la_lista(lista:list,elemento:str)-> list:
 aux= []
 for i in lista:
   a= i.replace(elemento,"")
   aux.append(a)
 return aux

if __name__ == "__main__":
  lista_frutas_dos=eliminar_un_caracter_de_toda_la_lista(lista_frutas,"\n")
  lista_frutas_sin_n= eliminar_un_caracter_de_toda_la_lista(lista_frutas_dos,"n")
  print(lista_frutas_sin_n)


#Realizar una funcion que retorne la copia de una funcion que pasa por parametro
"""
Entradas:
lista-->list-->lista

Salidas:
lista-->list-->lista
"""
def copia_lista(lista:list)-> list:
  return lista.copy() 

if __name__ == "__main__":
  copia=copia_lista(lista_numeros)
  lista_nueva= eliminar_un_caracter_de_toda_la_lista(copia,"\n")
  print(copia_lista(lista_numeros))

  

#Realizar una funcion que retorne una lista de numeros enteros   
"""
Entradas:
lista-->list-->lista

Salidas:
lista-->list-->lista
"""  

def numeros_enteros(lista:list):
  aux=[]
  aux2=[]
  for i in lista:
    aux.append(float(i))
  for i in aux:
    aux2.append(int(i))
  return aux2

if __name__ == "__main__": 
  lista_sin_espacio=eliminar_un_caracter_de_toda_la_lista(copia,"\n")
  print(numeros_enteros(lista_sin_espacio))


#Realizar una funcion que elimine un elemento de una lista
"""
Entradas:
lista-->list-->lista
elemento-->str-->elemento

Salidas:
lista-->list-->lista
"""  
def elimina_elemento_lista(lista:list,elemento:str)-> list:
  aux= []
  for i in lista:
    a= i.replace(elemento,"")
    aux.append(a)
  return aux

if __name__ == "__main__":
  lista_frutas_nueva=elimina_elemento_lista(lista_frutas,"\n")
  lista_frutas_sin_Uva=elimina_elemento_lista(lista_frutas_nueva,"Uva")
  print(lista_frutas_sin_Uva)


#Retorna una lista con las palabras iniciales con la letra que pasa por parametro  
"""
Entradas
letra-->str-->letra
lista-->list-->lista

Salidas:
lista-->list-->lista
"""
def letra(letra:str,lista:list)-> list:
  aux= []
  for i in lista:
    if (i[0]==letra):
      aux.append(i)
  return aux

if __name__ == "__main__":
  lista_inicial=letra("U",lista_frutas)
  print(lista_inicial))


#Realizar una funcion que retorne el tamaño de una lista
"""   
Entradas:
lista-->list-->lista
elemento-->str-->elemento

Salidas:
lista-->list-->lista
"""   
def tamano_lista(lista:list):
  tm= len(lista)
  aux= []
  for i in lista:
    aux.count(i==0)
  return tm

if __name__ == "__main__":
  print(tamano_lista(lista_numeros))


#Retorna el tamaño de la lista y que tipo de datos estan dentro de la lista
"""
Entradas:
lista-->list-->lista
numero-->int-->numero

Salidas:
lista-->list-->lista
""" 
def informacion_lista(lista:list):
  tm= len(lista)
  aux= []
  for i in lista:
    if(aux.count(i)==0):
      aux.append(type(i))
  return tm,aux

if __name__ == "__main__": 
  print(informacion_lista(lista_frutas))


#Retorne una lista con los numeros negativos
"""
Entradas:
lista-->list-->lista

Salidas:
lista-->list-->lista
"""
def numeros_negativos(lista:list):
  aux= []
  aux2= []
  for i in lista:
    aux.append(float(i))
  for i in aux:
    if(i<0):
      aux2.append(int(i))
  return aux2

if __name__ == "__main__": 
  lista_sin_espacio=eliminar_un_caracter_de_toda_la_lista(copia,"\n")
  print(numeros_negativos(lista_sin_espacio))


#Realizar una funcion que retorne la posicion de un elemento que pasa por parametro
"""
Entradas:
lista-->list-->lista
lista-->str-->elemento

Salidas:
lista-->list-->lista
"""
def posicion_elemento(lista:list,elemento:str):
  aux= []
  for i in lista:
    if (str(i)==str(elemento)+"\n"):
      aux.append(lista.index(i))
  return aux
  
if __name__ == "__main__": 
  print(posicion_elemento(lista_frutas,"Fresa"))

#Realizar una funcion que agregue al final de archivo frutas una fruta
"""
Entradas:
lista-list-->lista
lista-str-->elemento

Salidas:
lista-list-->lista
"""
def frutas_nuevo(elemento):
  frutas= open('frutas.txt', 'r')
  for i in frutas:
    lista_frutas.append(i)
  frutas.close()

  frutas= open('frutas.txt', 'w')

  for i in lista_frutas:
    frutas.write(i)

  frutas.write("\n"+str(elemento))
  frutas.close()

if __name__ == "__main__": 
  print(frutas_nuevo,"Granadilla")


#Realizar una funcion que cuente el numero de veces que se repite un elemento 
""" 
Entradas:
lista-list-->lista

Salidas:
lista-list-->lista
"""
def repetir(elemento):
  aux= []
  for i in elemento:
    aux.count(i=="123")
  return aux

if __name__ == "__main__":
  print(repetir(lista_numeros))
