
d = int(input("enter the day you got the vaccine"))
l = 90
r = l + 15

if(d < l):
    print("You are early for the vaccine")
elif(d > r):
    print("You are late for the vaccine")
elif(d >= l and d <= r):
    print("you are on time for the vaccine")
else:
    print("error in the value")