a1 = int(input("price of item 1"))
a2 = int(input("price of item 2"))
a3 = int(input("price of item 3"))

b1 = int(input("price of item 1 on next day"))
b2 = int(input("price of item 2 on next day"))
b3 = int(input("price of item 3 on next day"))

d = int(input("enter the delivery charge"))
c = int(input("enter the coupon charge"))

total1 = a1 + a2 + a3
total2 = b1 + b2 + b3

order1 = a1 + a2 + a3 + d
order2 = b1 + b2 + b3 + d

totalOrder = order1 + order2


if(total1 > 150):
    c1 = total1
else:
    c1 = order1

if(total2 > 150):
    c2 = total2
else:
    c2 = order2


totalOrderWithC = c1 + c2 + c

if(totalOrderWithC < totalOrder):
    print("user should buy the coupon")
elif(totalOrderWithC == totalOrder):
    print("user should not buy the coupon")
elif(totalOrderWithC > totalOrder):
    print("user should not buy the coupon")