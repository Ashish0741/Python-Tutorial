
# Exception Handling :

# Flow : Errors --> Exception

# Errors : syntax (won't handle)

# Exceptions : errors (runtime + compile time) (willingly handling)

# Bugs : unexpected output => add(5,10) ==> None

# =================================================================================

# Program 1 :

print("Start")

try:
    print(10/0)

except Exception as e:   # except Exception as e <==> e = Exception()
    print("Do not use zero for division")

print("End")

# ===================================================================================

print(40 * '=')

# Program 2 :  

print("Start")

try:
    l1 = [12,4,5,6,7]
    print(l1[10])

except Exception as e:
    print(e)

print("End")


# ===================================================================================

print(40 * '=')

# Program 3 :  

print("Start")

try:
    print(10 / 0)

except ArithmeticError as e:
    print("Block 1 : ",e)

except Exception as e:
    print("Block 2 : ",e)

print("End")


# ===================================================================================

print(40 * '=')

# Program 4 :  

print("Start")

try:
    print(10 / 0)
    
except IndexError as e:
    print("Block 1 : ",e)

except ZeroDivisionError as e:
    print("Block 2 : ",e)

print("End")


# ===================================================================================

print(40 * '=')

# Program 5 :  

# NOTE : Always write exception in specific to generic manner.

print("Start")

try:
    print(10 / 0)
    
except Exception as e: 
    print("Block 1 : ",e)

except ZeroDivisionError as e:  # this is wrongly written (This will throw compile time error)
    print("Block 2 : ",e) 

print("End")

# ===================================================================================

print(40 * '=')

# Program 6 :  

print("Start")

try:
    print(10 / 0)
    try:
        l1 = [1,2,3,4]
        print(l1[10])
    
    except Exception as e:
        print("Inner Block : ",e)

except Exception as e:
    print("Outer Block : ",e)

print("End")


# ===================================================================================

print(40 * '=')

# Program 7 :  

print("Start")

try:
    print(10 / 2)
    try:
        l1 = [1,2,3,4]
        print(l1[10])
    
    except Exception as e:
        print("Inner Block : ",e)

except Exception as e:
    print("Outer Block : ",e)

print("End")


# ===================================================================================

print(40 * '=')

# Program 8 :  

print("Start")

try:
    try:
        l1 = [1,2,3,4]
        print(l1[10])
    
    except Exception as e:
        print("Inner Block : ",e)
        print(10 / 0)

except Exception as e:
    print("Outer Block : ",e)

print("End")


# ===================================================================================

print(40 * '=')

# Program 9 :  

print("Start")

try:
    print(10 / 0)

except Exception as e:
    print("Except Block : ",e)

finally:
    print("Finally Block : Always executed -->  mainly used to close data resources")

print("End")


# ===================================================================================

print(40 * '=')

# Program 10 :  

print("Start")

try:
    print(10 / 2)

except Exception as e:
    print("Except Block : ",e)

finally:
    print("Finally Block : Always executed -->  mainly used to close data resources")

print("End")

# ===================================================================================

print(40 * '=')

# Program 11 :  

print("Start")

try:
    # print(10 / 0)   # this will throw error 
    pass

finally:
    print("Finally Block : Always executed -->  mainly used to close data resources")

print("End")


# ===================================================================================

print(40 * '=')

# Program 12 :  

print("Start")

try:
    print(10 / 2)

finally:
    print("Finally Block : Always executed -->  mainly used to close data resources")

print("End")


# ===================================================================================

print(40 * '=')

# Program 13 :  

print("Start")

try:
    try:
        l1 = [1,2,3,4]
        print(l1[10])
    
    except Exception as e:
        print("Inner Block : ",e)
        print(10 / 0)

    finally:
        print("This is inner finally")

except Exception as e:
    print("Outer Block : ",e)

finally:
    print("This is Outer finally")

print("End")

# ===================================================================================

print(40 * '=')

# Program 14 :  

print("Start")

try:
    print(10 / 2)
    try:
        l1 = [1,2,3,4]
        print(l1[10])
    
    except Exception as e:
        print("Inner Block : ",e)

    finally:
        print("This is Inner finally block")

except Exception as e:
    print("Outer Block : ",e)

finally:
    print("This is Outer finally block")

print("End")


# ===================================================================================

print(40 * '=')

# Program 15 :  

print("Start")

try:
    print(10 / 0)
    try:
        l1 = [1,2,3,4]
        print(l1[10])
    
    except Exception as e:
        print("Inner Block : ",e)

    finally:
        print("This is Inner finally block")

except Exception as e:
    print("Outer Block : ",e)

finally:
    print("This is Outer finally block")

print("End")


# =====================================================================================

print(20 * '=',"Custom Exception",20 * '=')
# Custom Exception : It is used when we need to terminate program on certain condition

# Program 1:

marks = 10

if marks < 35:
    print("Please try again")  # must terminate the program (throw exception)
    print("Other lines of code")

else:
    print("Proceed Further")


# =====================================================================================
print(40 * '=')
# Program 2 :

marks = 10

if marks < 35:
    pass
    # raise Exception("Please try again")
    # print("Other lines of code")   # this code is unreachable

# else:
#     print("Proceed Further")


# =====================================================================================

print(40 * '=')

# Program 3 :
# Creating custom Exception class and inherting with BaseException

class MyException(BaseException):
    def __init__(self, msg) -> None:
        print(msg)


marks = 10

if marks < 35:
    pass
#     raise MyException("Please try again")

# else:
#     print("Proceed Further")


# =====================================================================================

print(40 * '=')

# Program 4 :

# Calling init method of base exception by passing msg

# class MyException(BaseException):
#     def __init__(self, msg) -> None:
#         super().__init__(msg)


# marks = 10

# if marks < 35:
#     # pass
#     raise MyException("Please try again")

# else:
#     print("Proceed Further")


# ==========================================================================================






