a1 = int(input("enter the value of day 1"))
a2 = int(input("enter the value of day 2"))
a3 = int(input("enter the value of day 3"))
a4 = int(input("enter the value of day 4"))
a5 = int(input("enter the value of day 5"))
a6 = int(input("enter the value of day 6"))
a7 = int(input("enter the value of day 7"))

weather = a1+ a2+ a3+ a4+ a5+ a6+ a7

rainy =  7 - weather

if(weather > rainy):
    print("Yes")
elif(weather < rainy):
    print("No")

