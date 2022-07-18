x = int(input("enter the days needed to complete the first trip"))
y = int(input("enter the days needed to complete the second trip"))
z = int(input("enter the days of vaccation"))

complete = x + y

if(z == complete):
    print("YES")
elif(z > complete):
    print("YES")
elif(z < complete):
    print("NO")
