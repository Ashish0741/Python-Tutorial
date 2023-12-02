
# Static :

# void show(int num){
#     print("hello");
# }

# show(50);

# returnType function_name(parameters){
#     // body  --> logic of functions
# }

# function_calling

#----------------------------------------------------------------------------------

# Functions in python :

def show():
    print("hello")


show()

# Default function :

def default_func():
    print("This is default function.")


default_func()


# Parametarize function :

def add(num1,num2):
    print(num1 + num2)


add(10,45)


# Using return :

def sub(num1, num2):
    return num1 - num2  


print(sub(90,43))

def sub_two(num1, num2):
    return num1 - num2


result = sub_two(70,65)
print(result + 65)


# Default values in functions :

def default_values(num1 , num2 = 76):
    return num1 + num2


print(default_values(10))  # this will take num2 as default value
print(default_values(34,78))  # In this scenario num2 value will be overwrite by argument value

def display(num1 = 89, num2 = 90):
    return num1 - num2

print(display())   # in this case it will take both default values
print(display(67))


# keyword arguments : pass argument as key=value

def keyword_args(num1, num2):
    print(num1 * num2)


keyword_args(num1=67,num2=6)

keyword_args(num2=78,num1=5)   # can pass arguemnt in any order


# def keyword_args1(num1 = 7, num2):  # this will give compile time error as in python we can only set second parameter as default
#     print(num1 * num2)


# keyword_args1(num1 = 8, num2 = 2)


# Multi value inside single variable :

# *args : This will take multiple values as tuple

def args_example(*num):
    print(num)


args_example(10,34,56,7)  


# **kwargs : This will take mutiple values as dictionary

def kwargs_example(**pair):
    print(pair)


kwargs_example(name='Ashish', Age = 23)


# Looping Functions :

def outer_func():
    print("Outer Func")
    def inner_func():
        return 5

    inner_func()


print(outer_func())

# Output : 
# Outer Func
# None

def outer_func1():
    print("Outer Func")
    def inner_func1():
        return 5

    print(inner_func1())


print(outer_func1())

# Output : 
# Outer Func
# 5
# None


# returning entire inner_func()

def outer():
    print("This is outer function")
    def inner():
        return 5

    return inner  # this will return inner function reference


mynew_call = outer()  # here we store output of outer function i.e inner function in reference variable
print(mynew_call())   







