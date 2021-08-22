"""
Entradas
edad-->int-->edad
sexo-->str-->sexo
edad o meses-->str-->c
porcentaje de hemoglobina-->int-->h
Salidas
Resultado de la anemia-->int-->Resultado
"""
c=str(input("Digite 1 si tiene años o 2 si tiene meses: "))
edad=int(input("Escriba su edad: "))
h=int(input("Escriba su porcentaje de hemoglobina: "))
sexo=str(input("Digite 1 si es hombre o 2 si es mujer: "))
if (c==2):
    if (edad<=1 and h>=13):
        Resultado="No tiene anemia"
    else:
        Resultado="Tiene anemia"
    if ((edad>1 and edad<=6) and (h>=10)):
        Resultado="No tiene anemia"
    else:
        Resultado="Tiene anemia"
    if ((edad>6 and edad<=12) and (h>=11)):
        Resultado="No tiene anemia"
    else:
        Resultado="Tiene anemia"
else:
    if ((edad>=1 and edad<=5) and (h>=11.5)):
        Resultado="No tiene anemia"
    else:
        Resultado="Tiene anemia"
    if ((edad>5 and edad<=10) and (h>=12.6)):
        Resultado="No tiene anemia"
    else:
        Resultado="Tiene anemia"
    if ((edad>10 and edad<=15) and (h>=13)):
        Resultado="No tiene anemia"
    else:
        Resultado="Tiene anemia"
    if (edad>15):
        if (sexo==2):
            if (h>=12):
                Resultado="No tiene anemia"
            else:
                Resultado="Tiene anemia"
        else:
            if (h>=14):
                Resultado="No tiene anemia"
            else:
                Resultado="Tiene anemia"    
print("Estimado usted "+str(Resultado))
