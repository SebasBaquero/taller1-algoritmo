Algoritmo SueldoTotal_comision
	Definir sb, v1, v2, v3, com, total Como Real
	Escribir "ingrese su sueldo base"
	Leer sb
	Escribir "ingrese el valor de la venta1 "
	Leer v1
	Escribir "ingrese el valor de la venta2  "
	Leer v2
	Escribir "ingrese el valor de la venta3 "
	Leer v3
	com<-(v1+v2+v3)*0.10
	Escribir "la comision es de " com
	total<-com+sb
	Escribir "el suedo total seria de " total	
	
FinAlgoritmo
