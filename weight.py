w1 = int(input("Enter your previous weight"))
w2 = int(input("Enter your current weight"))

x1 = int(input("Enter minimmun weight increase"))
x2 = int(input("Enter maximum weight increase"))

m = int(input("Enter the number of months"))

inreased_weight = w2 - w1
min_increase = x1 * m
max_increase = x2 * m

if(inreased_weight == min_increase or inreased_weight == max_increase):
    print("1")
elif(inreased_weight > min_increase and inreased_weight < max_increase):
    print("1")
elif(inreased_weight < min_increase or inreased_weight > max_increase):
    print("0")

