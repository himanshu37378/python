
#printing
print("hwww")

#variable
x = "552"

y = "584"

print( x + y)

print(float(x) + float(y))



#getting user input

age = int(input("what is you age"))
print (age + x)
age1 = float(input("what is you age"))
print(age + age1)



#string

name = "Himanshu Mahajan"

print(name.upper())
print(name)
print(name.lower())
print(name.find('a'))
print(name.find('A'))
print(name.find("Mahajan"))
print(name.find('mahajan'))

print (name.replace("Himanshu Mahajan" , "Hello You"))
print(name)

print("Mahajan" in name)
print("M" in name)
print("Himnshuuu" in name)


#comparison operaors
 # + - * / ** %
print(1 > 5)
print(1 < 5)
print(8 != 5)
print(1 == 5)

#logical operators
print(not 1 == 5)

print(1 > 5 or 1 < 5)
print(6 > 5 or 1 < 5)

print(1 > 5 and 1 < 5)
print(1 < 5 and 1 < 5)


#if statements

age = 5

if (age < 10):
    print("you are young now")
    print("you are  now")

elif age < 3:
    print("you are a child")
else :
    print("not correct age ")



#simple calculator
first = int(input("Enter first number : "))
second = int(input("Enter second number : "))

print("----press keys for operator (+,-,*,/,%)----------")
operator = input("Enter operator : ")

if operator == "+":
   print(first + second)
elif operator == "-":
   print(first - second)
elif operator == "*":
   print(first * second)
elif operator == "/":
   print(first / second)
elif operator == "%":
   print(first % second)
else:
   print("Invalid Operation")




#range function

num = range(1+1, 11+1)
print(num)



#while loop

i = 1
while(i <= 5):
   print(i * "*")
   i = i + 1

#for loop
for i in range(10, 1 ,-1):
    print(i)

#lists
friends = ["himanshu" , "gupi" , "jaggu"]
print(friends)
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[-1])

friends[0] = "Mahajan"
print(friends)

print(friends[1:3])

for friend in friends:
    print(friend)


friends.append("amanjot")
print(friends)

friends.insert(0, "Chirag")
print(friends)
#printing list using for loop
for friend in friends:
    print(friend)

print(len(friends))
#printing list using while loop
i = 0
while i < len(friends):
    print(friends[i])
    i = i + 1

#break statement
for i in range(5):
    print(i)
    if(i == 3):
        break

#continue statement
for i in range(5):

    if(i == 3):
        continue
    print(i)

#tuples

marks = (12, 13, 15, 25)
print(marks[0])

print(marks.count(15))

print(marks.index(15))

#sets

marks = {15, 14, 17, 43}
print(marks)

for mark in marks:
    print(mark)

#dictionary

marks = {"math" : 99, "english" : 95, "hindi" : 89}
print(marks)

print(marks["english"])

marks["sst"] = 88
marks["science"] = 99
marks["english"] = 59

print(marks)


#functions

#in-built functions

#module functions
import math
print(dir(math))

#from math import pi
print(pi)

import random
print(dir(random))

#user defined functions
def hello():
    print("hello how are you!")

hello()


def addition(x,y,z):
    a = x + y
    b = x + z
    c = y + z
    print(a, b, c)

addition(5,6,7)





