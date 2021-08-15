"""
Entradas
Numero de niños-->int-->men
Numero de niñas-->int-->mujer
Salidas
Porcentaje de hombres-->int-->porcentaje1
Porcentaje de mujeres-->int-->porcentaje
"""
men= int(input("Escriba el numero de estudiantes hombres: "))
mujer= int(input("Escriba el numero de estudiantes mujeres: "))
suma= (men+mujer)
porcentaje= (mujer*100)/suma
porcentaje1= (men*100)/suma
print("El porcentaje de mujeres en el grupo es de ", porcentaje, "%")
print("El porcentaje de hombres en el grupo es de ", porcentaje1, "%")
