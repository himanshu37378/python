class Person(object):
   
  def __init__(self, name, id):
    self.name = name
    self.id = id
 
  def Display(self):
    print(self.name, self.id)
 

emp = Person("Himanshu", 102) 
emp.Display()

############################################################################################################################

# single inheritance

class Parent:
    def func1(self):
        print("This function is in parent class.")

class Child(Parent):
    def func2(self):
        print("This function is in child class.")


object = Child()
object.func1()
object.func2()

########################################################################################################################

# multiple inheritance
class Mother:
    mothername = ""

    def mother(self):
        print(self.mothername)

class Father:
    fathername = ""

    def father(self):
        print(self.fathername)

class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)


s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()

########################################################################################################################

# multilevel inheritance
class Grandfather:

    def _init_(self, grandfathername):
        self.grandfathername = grandfathername

class Father(Grandfather):
    def _init_(self, fathername, grandfathername):
        self.fathername = fathername


        Grandfather._init_(self, grandfathername)

class Son(Father):
    def _init_(self, sonname, fathername, grandfathername):
        self.sonname = sonname


        Father._init_(self, fathername, grandfathername)

    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print("Father name :", self.fathername)
        print("Son name :", self.sonname)


s1 = Son('Prince', 'Rampal', 'Lal mani')
print(s1.grandfathername)
s1.print_name()

########################################################################################################################

# Hierarchical inheritance
class Parent:
    def func1(self):
        print("hey")

class Child1(Parent):
    def func2(self):
        print("hello")

class Child2(Parent):
    def func3(self):
        print("hi")

object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()
########################################################################################################################

# hybrid inheritance
class School:
    def func1(self):
        print("what about u")


class Student1(School):
    def func2(self):
        print("hello world ")


class Student2(School):
    def func3(self):
        print("how r u")


class Student3(Student1, School):
    def func4(self):
        print("howz going")

object = Student3()
object.func1()




#############################################################################################################################



# polymorphism
class Human:
    def intro(self):
        print("hello Human")

    def flight(self):
        print("humans can fly fights")


class pilot(Human):
    def flight(self):
        print("Pilots can fly")


class airhostess(Human):
    def flight(self):
        print("airhostess do not fly")


obj_hum = Human()
obj_pil = pilot()
obj_ah = airhostess()

obj_hum.intro()
obj_hum.flight()

obj_pil.intro()
obj_pil.flight()

obj_ah.intro()

################################################################################################################################

#modules

from math import *
print("The value of pi is", pi)

import os
cwd = os.getcwd()
print("Current working directory:", cwd)

from datetime import date
my_date = date(2022, 7, 20)
print("Date", my_date)

################################################################################################################################
