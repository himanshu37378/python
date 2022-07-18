a = int(input("enter the feature 1"))
b = int(input("enter the feature 2"))

a1 = int(input("enter the feature 1 of first lang"))
b1 = int(input("enter the feature 2 of first lang"))

a2 = int(input("enter the feature 1 of second lang"))
b2 = int(input("enter the feature 2 of second lang"))

if( a == a1 or a == b1 and b == a1 or b == b1):
    print("1")
elif( a == a2 or a == b2 and b == a2 or b == b2):
    print("2")
else:
    print("0")