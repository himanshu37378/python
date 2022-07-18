m = float(input("enter the mass"))
h = float(input("enter the height"))

height = h * h

bmi = m / height

if(bmi <= 18):
    print("under weight")
elif(bmi in range(19, 24)):
    print("Normal weight")
elif(bmi in range(25, 29)):
    print("Over weight")
elif(bmi >= 30):
    print("Obesity")
else:
    print("enter a valid input")