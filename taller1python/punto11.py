"""
Entradas
Nombre del trabajador-->str-->nombre 
Hijos-->int-->hijos 
Horas trabajadas-->float-->h 
Valor cada hora-->float-->p 
Horas extras-->float-->he 
Salidas
Asiganaciones-->float-->asig=as1+as2+as3 
Impuestos-->float-->i=q1+q2+q3 
Pago dirigido al trabajador-->float-->pf=sueldo-i
"""

nombre=str(input("Escriba su nombre: "))
hijos=int(input("Escriba la cantidad de hijos que tenga: "))
h=float(input("Escriba las horas trabajadas: "))
p=float(input("Escriba el valor asiganado por hora trabajada: "))
he=float(input("Escriba las horas extras trabajas: "))

ph=p*h
as1=250000
as2=180000
as3=173000*hijos
p2=(p*0.25)+p
phe=p2*he
asig=as1+as2+as3
sueldo=asig+ph+phe
q1=(sueldo*0.05)
q2=(sueldo*0.02)
q3=(sueldo*0.07)
i=q1+q2+q3
pf=sueldo-i
print("Buen dia",nombre, "el total de las asignaciones dadas fueron de: ",asig, "y las deducciones son de: ",i, "y el sueldo neto del trabajador es de:",pf)
