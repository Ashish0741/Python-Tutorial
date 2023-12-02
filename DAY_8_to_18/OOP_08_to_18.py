
# OOP : 

# 1. Real time scenrio using programming language
# 2. It is way of writing code


# Examples :

# Customer (passbook) <== Relations ==> Bank
#                |             ||
#              data          Accounts (Saving / Current)

# In oop, 
# 1. Object holds the data (variables + methods)
# 2. Relations (Pillers)

# Class : It is diagram or blueprint or template

class Home():
    room = 2
    hall = 1
    kitchen = 1

    def washing_machine(self):
        print("This is washing machine.")

person1 = Home()
person2 = Home()
person3 = Home()

print(person1.hall)
print(person1.kitchen)
print(person1.room)

print(40 * '=')

print(person2.hall)
print(person2.kitchen)
print(person2.room)

print(40 * '=')

print(person3.hall)
print(person3.kitchen)
print(person3.room)

print(40 * '=')

person3.washing_machine()

print(40 * '=')

class MyClass:

    num = 10

    def access(self):
        print(self.num)

m1 = MyClass()
m1.access()
print(type(m1))
print(type(MyClass))

print(40 * '=')


# ===================================================================================================================

# Self : it denotes current calling object.

class Test:

    def show(self):
        print("This is example of self.")
        # print(self)

m1 = Test()  
m1.show()   # this will pass object as argument
# Test.show(m1)   # --> This is how it works

m2 = Test()
m2.show()

# -----------------------------

class Home:
    area = 100
    room = 2
    kitchen = 1


ashish = Home()
shivani = Home()

print(ashish.area)
print(shivani.area)

# shivani.area = 230   Don't do this type of manipulation as it creates copy of existing object
# Do not access static variable.

print(ashish.area)
print(shivani.area)


# -----------------------------------

class MyClass:
    # TypeError: MyClass.show() takes 1 positional argument but 2 were given
    def show(self):  # --> this will throw an error as we are passing list and by default object is also getting passed but in parameter we are only taking one parameter
        print(self)

lis = [10,3,4,5]
# new = MyClass()
# new.show(lis)    

# ------------------------------------

# Properties :
# 1. Static (class bounded)
# 2. Instance (object bounded)


class Home:
    # static variable
    area = 100   # creates area static variable in shared memory inside class memory
    
print(Home.area)  

ashish = Home()
sahil = Home()

print(ashish.area)
print(sahil.area)

sahil.area = 980   # This will create new copy of area in object sahil in heap memory 
ashish.area = 90   # This will create new copy of area in object ashish in heap memory 

# Always avoid to do above scenrio

print(ashish.area)
print(sahil.area)


# --------------------------------------------

class Home:
    area = 100
    
print(Home.area)

h1 = Home()
h2 = Home()

h1.area = 80  # Instance variable 
h2.area = 90  # Instance Variable

print(h1.area)
print(h2.area)
print(Home.area)


# ------------------------------------------------

# Instance variables (Object bounded) :

class Home:
    def __init__(self,room,hall):
        self.final_room = room   # this creates instance variable in heap memory
        self.final_hall = hall
        
h1 = Home(3,2)
h2 = Home(4,5)

print(h2.final_room)  # Inside constructor all are instance variables that can access only by object

print(10 * '-')

# ----------------------------------------------------------

# Different types of variables :

class Home:

    area = 100    # static variable

    def __init__(self,room,hall) -> None:
        # room --> local variable
        self.room = room    # instance variable
        self.hall = hall    # instance variable

h1 = Home(3,2)
h2 = Home(4,5)

print(h2.room)

# --------------------------------------------------------

# What is constructor ?

# 1. It is called automatically & separately for each object when object is created

class Test:

    def __init__(self) -> None:
        print("Constructor is invoked.")

h1 = Test()


# 2. Doesn't return anything

class Test:

    def __init__(self) -> None:
        # return "Constructor is invoked."  --> TypeError: __init__() should return None, not 'str'
        pass

h2 = Test()


# 3. Object init (to provide values inside the object)


class Home1:

    def __init__(self,room,hall) -> None:
        self.room = room 
        self.hall = hall

home = Home1(3,2)

print(home.room)


# --------------------------------------------------------------

# Can we call constructor explicitly ??

# --> We cannot call constructor explicitly but python allow us to call .


class Test1:

    def __init__(self) -> None:
        print("Calling constructor explicitly.")

test1 = Test1()
test1.__init__()   # calling explicitly


#  --> But in python we do not have constructor __init__() is special method for object initiation.


class Test1:

    # __init__() is special method for object init in python

    def __init__(self) -> None:
        print("This is special method for object init.")

test1 = Test1()


# ----------------------------------------------------------------------

# Question :

# 3 Minor pillars of OOP : Association, Aggregation and Composition

class Laptop:
    def __init__(self,cam,hdd,proc,logo) -> None:
        self.cam = cam
        self.hdd = hdd
        self.proc = proc
        self.logo = logo

class Camera:
    def __init__(self,sensor,mp) -> None:
        self.sensor = sensor
        self.mp = mp

class HDD:
    def __init__(self,storage,type) -> None:
        self.storage = storage
        self.type = type

class Processor:
    def __init__(self,pname,pgen) -> None:
        self.pname = pname
        self.pgen = pgen

cam1 = Camera("Wide Angle", 60)
hdd1 = HDD(250,"DDR2")
proc1 = Processor("Intel", "i7")

person1 = Laptop(cam1,hdd1,proc1,"HP")
break_line = '\n'
print(f"Laptop Name : {person1.logo}")
print(f"Specifications :{break_line}\
    Camera : 1. Sensor : {person1.cam.sensor} , 2. MP : {person1.cam.mp}{break_line}\
    HDD : 1. Type : {person1.hdd.type} , 2. Storage : {person1.hdd.storage}{break_line}\
    Processor : 1. Name : {person1.proc.pname} , 2. Generation : {person1.proc.pgen}")

print(10 * '-')

cam2 = Camera("Wide Angle", 90)
hdd2 = HDD(500,"DDR4")
proc2 = Processor("Intel", "i9")

person2 = Laptop(cam2,hdd2,proc2,"Asus")
break_line = '\n'
print(f"Laptop Name : {person2.logo}")
print(f"Specifications :{break_line}\
    Camera : 1. Sensor : {person2.cam.sensor} , 2. MP : {person2.cam.mp}{break_line}\
    HDD : 1. Type : {person2.hdd.type} , 2. Storage : {person2.hdd.storage}{break_line}\
    Processor : 1. Name : {person2.proc.pname} , 2. Generation : {person2.proc.pgen}")


# --------------------------------------------------------------------------------------------

print(10 * '-',"DAY 14",10 * '-')

# Special Methods (re-define), dunder methods :

# When we print object what happens behind the scene ?

# Ans : When we print object behind the scene it invokes __str__() method which gives object in form of string

class PrintObject:
    def __init__(self,num) -> None:
        self.num = num


obj = PrintObject(6)
print(obj)
print(obj.__str__())


# -------------------------------------------------------

# we can overwrite the __str__() method 

class OverWriteStrMethod:
    def __init__(self,num) -> None:
        self.num = num

    def __str__(self) -> str:
        return "str method invoked."


obj = OverWriteStrMethod(6)
print(obj)
print(obj.__str__())

# -----------------------------------------------------------

class OverWriteStrMethod:
    def __init__(self,num) -> None:
        self.num = num

    def __str__(self) -> str:
        # TypeError: __str__ returned non-string (type int)
        # NOTE : __str__() method can return only string

        # return self.num

        return "__str__() method can return only string"


obj = OverWriteStrMethod(6)
print(obj)

# -------------------------------------------------------------------

# 4 Major Pillars of OOP :
# ===============================================
# 1. Encapsulation : It is represent class.
# ===============================================

# It provides (data binding) + (security[access specifiers])

# Access Specifiers : public (default), protected and private

# 1. public => synatx : name => this can be access from anywhere within scope.
# 2. protected => syntax : _name (use one underscore) => pending 
# 2. private => syntax : __name (use 2 underscore) => this can be access within scope of class.

class TestEncap:

    # NOTE : private variable or methods can be access within class scope

    age = 23   # public variable
    _name = "Ashish"    # protected variable
    __city = "Mumbai"   # private variable
    

    def __init__(self,state) -> None:
        self.__state = state

    def __show(self):    # private method
        print("This is private method.")

obj1 = TestEncap("M.H.")
# print(obj1.city)  --> This will give error as we are trying to access private static variable
# obj1.__show()   --> above error will be given in this method too as it is private method
print(obj1._name)   # --> This will give output as it is protected variable it can access out of class scope

# ------------------------------------------------------------------------------------

# We can access private variable or method using public method :

class TestEncap1:
    
    def __init__(self,city,state) -> None:
        self.__state = state
        self.__city = city

    def __show(self):
        print("This is private method.")

    def display(self):
        print(self.__city,self.__state)
        self.__show()


obj3 = TestEncap1("Mumbai","M.H.")
obj3.display()

# ---------------------------------------------------------------------------------------

# Getter and Setter Methods :

# Getter : Retrive values from object

# Setter : Provide values inside object

# We can access private members through getter and setter
# This can be used for validations
# To provide read write access

# class GetSet:

#     __name = None
#     __age = 0

#     def setName(self,name):
#         self.__name = name

#     def getName(self):
#         return self.__name

#     def setAge(self,age):
#         self.__age = age

#     def getAge(self):
#         return self.__age

# obj4 = GetSet()
# obj4.setName("Ashish")
# print(obj4.getName())
# obj4.setAge(23)
# print(obj4.getAge())

# obj5 = GetSet()
# obj5.setName("Shivani")
# print(obj5.getName())
# obj5.setAge(24)
# print(obj5.getAge())

# ----------------------------------------------------------------------

class GetSet:

    def __init__(self,name = None,age = 0) -> None:
        self.__name = name
        self.__age = age

    def setName(self,name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAge(self,age):
        self.__age = age

    def getAge(self):
        return self.__age

obj4 = GetSet()
obj4.setName("Ashish")
print(obj4.getName())
obj4.setAge(23)
print(obj4.getAge())

# ---------------------------------------------------------------

import re

class SearchWord:

    def __init__(self,name = None) -> None:
        self.__name = name

    def getName(self):
        return self.__name

    def setName(self,name,find):
        match = re.search(name,find)    # Takes only string as parameter
        if match:
            self.__name = name


find = "ashish shivani yash saloni"
obj5 = SearchWord()
obj5.setName("ash",find) 
print(obj5.getName())

# ------------------------------------------------------------------


print(20 * '-',"Inheritance",20 * '-')

# ====================================================================
# 2. Inheritance : It is mainly used for code reusability.
# ======================================================================

# I. Simple Inheritance :

class Parent:
    def parent_method(self):
        print("This is parent method")

class Child(Parent):
    pass

child = Child()
child.parent_method()

# ------------------------------------------------------

class Parent:
    def __init__(self):
        print("This is parent method")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("This is child method")

child = Child()

# --------------------------------------------------------
class Parent:
    num = 987

class Child(Parent):
    pass

# child0 = Child()
print(Child.num)
    
# -----------------------------------------------------

# II. Multilevel Inheritance :

class GParent:

    name = "Ashish"

    def __init__(self) -> None:
        self.num  = 10

    def grant_parent_method(self):
        # self.num  = 10
        print("This is gparent method")

class Parent(GParent):
    def parent_method(self):
        print(self.num)  # we can access instance variable using self.
        # print(super().num)  # we cannot access parent instance variable too. only methods can be called using super 
        self.grant_parent_method()  # calling gparent method using self (Parent)
        super().grant_parent_method()   # calling gparent method using super (GParent) keyword 
        print("This is parent method")


class Child(Parent):
    def child_method(self):
        print(super().name)
        print(self.name)  # we can access static variable using self.
        print(self.num)  # we can access static variable using super too.
        print("This is child method")

child1 = Child()
child1.child_method()
child1.parent_method()
child1.grant_parent_method()

# -----------------------------------------------------
print(40 * '-')


# III. Multiple Inheritance: 


# class ParentOne:
#     def parent_one_method(self):
#         print("this is parent one method")

# class ParentTwo():
#     def parent_two_method(self):
#         print("this is parent two method")

# class Child(ParentTwo,ParentOne):
#     def child_method(self):
#         print("This is child method")

# child2 = Child()
# child2.parent_one_method()
# child2.parent_two_method()
# child2.child_method()



class ParentOne:
    name = "Shivani"
    def __init__(self) -> None:
        self.age = 23

    def parent_one_method(self):
        # self.age = 23
        print("this is parent one method")

class ParentTwo():
    def __init__(self) -> None:
        self.age = 22
    # name = "Ashish"
    # def parent_two_method(self):
    #     print("this is parent two method")
    pass

class Child(ParentTwo,ParentOne):   # This follow tree DS concept first left one will be taken then right one
    def child_method(self):
        print(self.name)  # can access static variable through self
        print(self.age)  # can access instance variable through self
        print(super().__init__())  # --> super method work for init method only
        print("This is child method")
        # print(ParentOne.name) 

child2 = Child()
# child2.parent_one_method()
child2.child_method()

# -----------------------------------------------------------

class Parent:
    name = "Ashish"
    def __init__(self,surname):
        print("This is parent class")
        self.surname = surname

class Child(Parent):
    def __init__(self):
        print(super().name)
        # print(super().surname) 
        super().__init__("Khedekar")
        print("This is child class")
    
    
child = Child()
print(child.surname)

# -------------------------------------------------------------

print(40 * '-')


# IV. Hybrid Inheritance :
# NOTE : super keyword can go upto 1 level only

class GParent:
    def __init__(self) -> None:
        print("This is grand parent method")

class ParentOne(GParent):
    name = "Shivani"
    def __init__(self) -> None:
        self.age = 23
        super().__init__()

    def parent_one_method(self):
        # self.age = 23
        print("this is parent one method")

class ParentTwo(GParent):
    name = "Ashish K"
    def __init__(self) -> None:
        self.age = 22
        super().__init__()   
    # name = "Ashish"
    # def parent_two_method(self):
    #     print("this is parent two method")

class Child(ParentTwo,ParentOne):   # This follow tree DS concept first left one will be taken then right one
    def child_method(self):
        print(self.name)  # can access static variable through self
        print(self.age)  # can access instance variable through self
        # print(super().__init__())  # --> super method work for init method only
        print("This is child method")
        # print(ParentOne.name) 

child2 = Child()
# child2.parent_one_method()
child2.child_method()


print(20 * '-',"Polymorphism",20 * '-')

# ========================================================================
# 3. Polymorphism : It means many forms 

# behave -> friends behave, family behave and workplace behave . 
# ==========================================================================

# There are 4 types :

# I. Method Overriding (Redefining):

# --> 2 classes having relationship of inheritance
# --> Each classes must have same method name with same signature

class Parent:

    def bike(self):
        print("Black bike")

class Child(Parent):

    def bike(self):
        print("White bike")
    # pass

ch = Child()
ch.bike()

# --------------------------------------------------

class Parent:

    def bike(self):
        print("Black bike")

class Child(Parent):

    # def bike(self):
    #     print("White bike")  if we didn't write bike here then it will invoke parent cls bike method
    pass

ch = Child()
ch.bike()

# -----------------------------------------------------

class One:

    def bike(self):
        print("TVS")

class Two(One):

    # here parent cls bike method will get overwrite 
    def bike(self,name):
        print(name)

two = Two()
# two.bike()  --> this is throw error as seen above bike method gets overwrite so will need one argument.
two.bike("Ninja")

# --------------------------------------------------------

print(40 * '=')

# II. Method Overloading (This is will not happen in python... need to do in other way):

# --> 1 class having atleast 2 methods
# --> Methods must have same name and different count of parameter


class MethodOverloading:

    def add(self,num1,num2):
        print(num1 + num2)

    def add(self,num1,num2,num3):  # this add method will overwrite above add method as they are same method name
        print(num1 + num2 + num3)

ch = MethodOverloading()
# ch.add(10,20)
ch.add(10,20,30)

# ---------------------------------------------------------------------

# We can achieve method overloading in 2 ways :
# 1. By giving default parameter
# 2. By *args 
# 3. using dispatch


class MethodOverloading:

    def add(self,num1=0,num2=0,num3=0):
        print(num1 + num2 + num3)

ch = MethodOverloading()
print("By giving default parameter :")
ch.add(10,20)
ch.add(10,20,30)

# ----------------------------------------------------------------------
class MethodOverloading:

    def add(self,*nums):
        res = 0
        for num in nums:
            res += num

        print(res)

ch = MethodOverloading()
print("By using *args :")
ch.add(10,20)
ch.add(10,20,30)

# --------------------------------------------------------------------------
from multipledispatch import dispatch

class MethodOverloading:

    @dispatch(int,int)
    def add(self,num1,num2):
        print(num1 + num2)

    @dispatch(int,int,int)
    def add(self,num1,num2,num3): 
        print(num1 + num2 + num3)

ch = MethodOverloading()
print("using dispatch decorator :")
ch.add(10,20)
ch.add(10,20,30)


# ---------------------------------------------------------------------------

print(40 * '=')

# III. Operator Overloading :

class Number:

    def __init__(self,num) -> None:
        self.num = num

    def __add__(self,other):      # opertor overloading
        return (self.num + other.num)

    def __mul__(self,other):     # opertor overloading
        return self.num * other.num

num1 = Number(10)
num2 = Number(2)
print(num1.num + num2.num)
print("Addition :",num1 + num2)  
print("Multiplication :",num1 * num2)

# ---------------------------------------------------------------------

class Number:

    def __init__(self,num) -> None:
        self.num = num

    def __ne__(self,other):      # opertor overloading
        return self.num != other.num


num1 = Number(10)
num2 = Number(10)
print(num1 != num2)

# --------------------------------------------------------------------------

print(40 * '=')

# IV. Duck Typing :

# --> It is concept related to dynamic typing, where the type or the class of an object is less important than the methods it defines. 
# --> When you use duck typing, you do not check types at all. Instead, you check for the presence of a given method or attribute.

class Human:
    def overthinker(self):
        print("This is a human")


class Animal:
    def caring(self):
        print("This is an animal")


class Aliean:
    def fly(self):
        print("This is an aliean")

ashish = Human()
simba = Animal()
jaadu = Aliean()


def room(take_obj):
    take_obj.fly()
    # take_obj.caring()
    # take_obj.overthinker()

room(jaadu)

# ----------------------------------------------------------------------

class DuckTyping:

    def __len__(self):
        return 90

duck = DuckTyping()
print("len of duck : ",len(duck))

list1 = [1,2,3,4,5]
print("len of list : ",len(list1))

str1 = "Aashish"
print("len of string : ",len(str1))

num = 10
# print("len of int : ",len(num))

# =========================================================================================

print(20 * '-',"Abstraction",20 * '-')

# 4. Abstraction : Data hiding ( to enforce subclasses to implement its parent class properties ).

# Eg. : Laptop [screen + keyboard]
#       Hide [hdd + motherboard]

# Abstract class :
# 1. abstract method (method w/o body) --> only declaration
# 2. can not create object of abstract class
# 3. subclass of abstract class must be implemented (provide body) abstract method.
# 4. In python to perform abstraction we need to inherit ABC class and declare one abstract method using decorator.

# Importing :

import importing  # this will import all the func, class and objects and variable which will take processing time

print(importing.num)

# ---------------------------------------------------

from importing import MyClass   # this will only MyClass

print("Importing which ever needed :")
obj = MyClass()
obj.show()

# ------------------------------------------------------

from importing import MyClass as Cls  # this will only MyClass

print("Using alias :")
obj = Cls()
obj.show()        

# --------------------------------------------------------

from abc import ABC, abstractmethod

class Abs(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

# obj = Abs()  # TypeError: Can't instantiate abstract class Abs with abstract method abstract_method
# obj.abstract_method()  --> This will as we have not yet fulfilled the condition of abstract method

class Test(Abs):
    def abstract_method(self):
        print("This body of abstract method...")

obj_abs = Test()
obj_abs.abstract_method()

# ---------------------------------------------------------

class Abs(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

    def __init__(self) -> None:   # this will get invoked as Child class don't have init method 
        print("This is init method inside abstract class")

class Child(Abs):
    def abstract_method(self):
        print("This body of abstract method...")

obj_abs = Child()
obj_abs.abstract_method()

# ------------------------------------------------------

print(40 * '-')

class Abs(ABC):
    name = "Ashish"

    @abstractmethod
    def abstract_method(self):
        pass

    def simple_nethod(self):
        print("this is normal method")

    def __init__(self,age) -> None: 
        self.age = age

class Test(Abs):
    def __init__(self) -> None:
        super().__init__(23)
        print(self.name)
        print("Using super name: ",super().name) # only static variable can be access using super
        # print("Using super age: ",super().age)

    def abstract_method(self):
        print(self.name)
        print("This body of abstract method...")

obj_abs = Test()
obj_abs.abstract_method()
obj_abs.simple_nethod()
# print(obj_abs.age,obj_abs.name)
# print(Abs.name)

# --------------------------------------------------------------------------

print(40 * '-')

# Method Types :

class MethodTypes:

    name = "Ashish"

    # self => current object
    def instance_method(self):
        print("This can only access by object and take memory inside object separately.")

    # cls => class
    @classmethod
    def class_method(cls):
        print("This can only access by class and take memory inside class only once.")
        cls.name = "Shivani"  # we can manipulate static variable through class method
        # cls.static_method()  # we usually use static in class method

    @staticmethod
    def static_method():
        print("This can only access by class and take memory inside class only once.")
        print("Provides behviour to class only.")

print("This can accessible using objects :")
obj_mt = MethodTypes()
obj_mt.static_method()
print(obj_mt.name)
obj_mt.class_method()
print(obj_mt.name)
obj_mt.instance_method()

print("Accessing using class :")
MethodTypes.static_method()
print(MethodTypes.name)
MethodTypes.class_method()
print(MethodTypes.name)

# MethodTypes.instance_method() --> this cannot be called using class 

# -----------------------------------------------------------------------------------