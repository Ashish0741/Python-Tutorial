
# Decorators : It is nothing but one function

# stage 1: take agrument in form of function reference
# stage 2: having inner function
# stage 3: return inner function reference

# ===========================================================================================

print(40 * '=')

# Program 1 : 

def deco_func(take_func_ref):   # stage 1: take agrument in form of function reference
    def inner_func():           # stage 2: having inner function
        print("This is inner function of decorator")
        take_func_ref()         # stage 3: calling function reference
    
    return inner_func           # stage 4: return inner function reference

def func():
    print("This is normal function")

func = deco_func(func)
func()


# ===========================================================================================

print(40 * '=')

# Program 2 : 

def deco_func(take_func_ref):  
    def inner_func():     
        print("This is inner function of decorator")   
        take_func_ref()
    
    return inner_func

@deco_func    # other way to call decorator
def func():
    print("This is normal function")


func()


# ===========================================================================================

print(40 * '=')

# Program 3 : 

def swap(divde_ref):
    def inner(*args, **kwargs):
        # print(args,kwargs)
        num1 = args[0]
        num2 = args[1]
        if num2 > num1:
            num1,num2 = num2,num1

        divde_ref(num1, num2)

    return inner

@swap
def divide(num1,num2):
    print(num1 // num2)

divide(2,10)


# ===========================================================================================

print(40 * '=')

# Program 4: 

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Bob")


# ===============================================================================================
