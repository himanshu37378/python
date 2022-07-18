a = int(input("enter the weight"))
b = int(input("enter the weight"))
c = int(input("enter the weight"))

d = int(input("enter the checked limit"))
e = int(input("enter the carry limit"))

if( a + b <= d and c <= e):
    print("yes")
elif(a + c <= d and b <= e):
    print("yes")
elif(b + c <= d and a <= e):
    print("yes")
else:
    print("no")


