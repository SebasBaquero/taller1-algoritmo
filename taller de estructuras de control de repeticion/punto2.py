"""
Salidas
contador de numeros-->int-->cn
"""
cn=0
while True:
    cn= cn+1
    if (cn%7==0):
        continue
    elif (cn%2==0):
        continue
    elif (cn>=100):
        break
    print(cn)
