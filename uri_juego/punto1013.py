input1 = input ().split(" ")
a, b, c = input1
a=int(a)
b=int(b)
c= int(c)
mayor = int((a+b)+abs (a-b))/2
maior1 = int((mayor+c)+ abs (mayor-c))/2
print(int(maior1), "eh o maior")
