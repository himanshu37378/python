###################################################################################
#Encapsulation
class Computer:
    def __init__(self):
        self.__maxprice = 900
    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))
    def setMaxPrice(self, price):
        self.__maxprice = price
c = Computer()
c.sell()
c.__maxprice = 1000
c.sell()
c.setMaxPrice(1000)
c.sell()


# public members & public access modifier
class pub_mod:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def Age(self):

        print("Age: ", self.age)

obj = pub_mod("Himanshu", 20)
print("Name: ", obj.name)
obj.Age()


########################################################################################################################

# Get and Set method to access private variables
class Person:
    def _init_(self, name, age):
        self.name = name
        self.__age = age

    def display(self):
        print(self.name)
        print(self.__age)

    def getAge(self):
        print(self.__age)

    def setAge(self, age):
        self.__age = age


person = Person("Himanshu", 18)
person.display()
person.setAge(20)


###################################################################################

#abstration
from abc import ABC, abstractmethod

class Animal(ABC):

    def sleep(self):
        print("I am going to sleep in a while")

    def sound(self):
        print("This function is for defining the sound by any animal")

class Snake(Animal):
    def sound(self):
        print("I can hiss")

class Dog(Animal):
    def sound(self):
        print("I can bark")

class Lion(Animal):
    def sound(self):
        print("I can roar")

class Cat(Animal):
    def sound(self):
        super().sound()
        print("I can meow")


c = Cat()
c.sleep()
c.sound()

c = Snake()
c.sound()


###################################################################################

#try
try:
  print(x)
except:
  print("An exception occurred")
#else
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

###################################################################################

#finally
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

###################################################################################
# the statement will raise an error because x is not defined
try:
  print(x)
except:
  print("An exception occurred")

########################################################################################################################

# try block does not raise any error so the else block is executed
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

########################################################################################################################

# finally block will be executed no matter if try block raises any error or not
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

########################################################################################################################

# Raise an error and stop the program if x is lower than 0
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")

########################################################################################################################
x=int(input("x : "))
y=int(input("y : "))
try:
  result = x // y
except ZeroDivisionError:
    print("Sorry ! You are dividing by zero ")
else:
    print("Yeah ! Your answer is :", result)
finally:
    print('This is always executed')

###################################################################################

#error raising
x = "hello"
if not type(x) is int:
     raise TypeError("Only integers are allowed")
