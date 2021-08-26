"""
Entradas
incremento de valor de EXP de monstruos-->x
el valor EXP del monstruo-->m
"""
while True:
    x, m = input().split()
    if(x == '0' and m == '0'):
        break
    print(int(x)*int(m))
