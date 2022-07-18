x = int(input("enter the current points"))
y = int(input("enter the points to win"))
z = int(input("enter the matches left "))

winpts = y - x


if( z * 2 >= winpts or z * 1 >= winpts or z * 0 >= winpts):
    print("RCB can win")
else:
    print("rcb can not win")

"""
if( z * 2 >= winpts):
    print("rcb can win")
elif(z * 1 >= winpts):
    print("rcb can win")
elif(z * 0 >= winpts):
    print("rcb can win")
else:
    print("rcb can not win")
    """