a = int(input("enter the brick1"))
b = int(input("enter the brick2"))
c = int(input("enter the brick3"))

s = int(input("enter the strength"))

total = a + b + c

if(total <= s):

    print("1")
elif(s >= a + b or s >= b + c):
    print("2")
else:
    print("3")


