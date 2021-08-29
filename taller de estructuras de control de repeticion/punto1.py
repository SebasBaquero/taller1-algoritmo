"""
Entradas
Dato N-->int-->n
Dato K-->int-->k
Salidas
datos result-->int-->n-1
"""
n=int(input("N: "))
k=int(input("K: "))
while True:
    if (k<n):
        print(n)
        n=n-1
    else:
      break
