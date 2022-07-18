import math

n = int(input("enter the number of floors"))
v1 = int(input("enter the velocity on stairs"))
v2 = int(input("enter the velocity on lift"))

stairs = (math.sqrt(2) * n) / v1
lift = 2 * n /v2

if(stairs > lift):
    print("lift")
elif(lift > stairs):
    print("stairs")
