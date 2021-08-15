"""
Entradas
cantidad chelines austriacos-->float-->ca
cantidad dracmas griegos-->float-->dg
cantidad pesetas--> float-->p
Salidas
pesetasr-->result= ca* chelin
francosFrances-->result1a= result1/ franco
dolares-->result2= p/dolar
liras-->p/v100liras
"""
peseta=1
v100chelines=956.871
chelin=v100chelines/100
v100dracma=88.607
dracma=v100dracma/100
franco=20.110
dolar=122.499
v100liras=9.289
liras=v100liras/100

ca=float(input("Digite una cantidad en chelines austriacos: "))
result= ca* chelin

dg=float(input("Digite una cantidad en dracmas griegos: "))
result1= dg* dracma
result1a= result1/ franco

p=float(input("Digite una cantidad en pesetas: "))
result2= p/dolar
result2a= p/v100liras

print("De chelines austriacos a pesetas es: ",result)
print("De dracmas griegos a francos franceses es: ",result1a)
print("De pesetas a dólares",result2, "liras italianas. es: ",result2a)
