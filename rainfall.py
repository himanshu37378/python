n = int(input("enter the number of days"))
d = int(input("enter the decrimenting value"))
h = int(input("enter the red alert limit"))
val = 0
for i in range(n):
    a = int(input("enter the value of rainfall"))
    if(a > 0):
        val = val + a
    elif(a == 0 and val != 0):
        val = val - d
    elif(a == 0 and val == 0):
        val = val

if(val > h):
    print("red alert")
else:
    print("no alert")


