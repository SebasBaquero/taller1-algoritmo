Algoritmo minutos_horas
	Definir m, h, h1, m1, m2 Como Real
	Escribir "escriba una cantidad de minutos"
	Leer m	
	h<- m/60
	h1=trunc(h)
	m1=(h-h1)*60
	m2=trunc(m1)
	Escribir "los minutos escritos en horas son:  " h1 "   horas y  " m2  "   minutos" 	
FinAlgoritmo
