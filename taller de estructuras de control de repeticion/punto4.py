"""
Salidas
Doceavo-->int-->doc
Suma-->int-->suma
"""
doc=0
for a in range(1,13):
  if(a>=1):
    doc=5*a+1
    if(doc==61):
      suma=(doc+6)*6
      print("a12= "+str(doc))
      print("suma= "+str(suma))
  elif(a==13):
    break
