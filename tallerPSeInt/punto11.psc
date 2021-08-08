Algoritmo notas_algoritmos
	Definir n1, n2, n3, ef, tf, parciales, nf Como Real
	Escribir "escriba sus tres calificaciones de los parciales"
	Leer n1, n2, n3
	Escribir "escriba la calificacion de su examen final"
	Leer ef
	Escribir "escriba la calificacion de su trabajo final"
	Leer tf
	parciales<-(n1+n2+n3)/3
	nf<-(parciales*0.55)+(ef*0.3)+(tf*0.15)
	Escribir "su nota final es   "  nf
	
FinAlgoritmo
