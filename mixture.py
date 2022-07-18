a = int(input("enetr the units of solid"))
b = int(input("enetr the units of liquid"))

if( a > 0 and b > 0):
    print("Solution")
elif(a == 0 and b > 0 ):
    print("liquid")
elif( a > 0 and b == 0):
    print("solid")
