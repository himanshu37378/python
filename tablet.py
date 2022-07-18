b = int(input("Enter your budget"))
n = int(input("enetr the number of tablets you choosed"))
tab = 0
for i in range(n):

    w = int(input("enter the width of the tablet"))
    h = int(input("enter the height of the tablet"))
    p = int(input("enter the price of the tablet"))
    a = w * h
    if(p <= b):
        if(a > tab):
            tab = a


if(tab == 0):
    print("no tablet")
else:
    print(tab)




