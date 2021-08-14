p1_code, p1_unit, p1_price = map(float, input().split())
p2_code, p2_unit, p2_price = map(float, input().split())

total = (p1_unit * p1_price) + (p2_unit * p2_price)
print("VALOR A PAGAR: R$ %.2f" % total)
