import math as ma
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
place_1= x2 - x1
place_2= y2 - y1
distance= ma.sqrt(pow(place_1, 2)+pow(place_2, 2))
print("%.4f" % distance)
