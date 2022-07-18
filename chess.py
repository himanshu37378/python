a = int(input("enter the avlue of a"))
b = int(input("enter the value of b"))

add = a + b

if add < 3:
    print("bullet")
elif add >= 3 and add <= 10:
    print("blitz")
elif add >= 11 and add <= 60:
    print("rapid")
elif add > 60:
    print("classical")