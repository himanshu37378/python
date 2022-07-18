x = int(input("Enter the time taken by the palne"))
y = int(input("Enter the time taken by the bus"))
z = int(input("Enter the time taken by the direct train"))

xy = x + y

if(xy == z):
    print("the time with both the routes are equal")
elif(xy > z):
    print("train takes less time")
elif(xy < z):
    print("Plane and bus takes less time")