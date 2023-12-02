
# File Handling :

# file --> data (.txt,.mp4,etc)

# handling --> operations (read, write and update)

# f1 = open("file1.txt","w")
# f1.write("This is first program of file handling")  # --> string

# This is continue from last write function output
# f1.writelines(["This is another method of writing in file\n","Please check"])   # string inside list object

# f1 = open("file1.txt","a")
# f1.writelines(["This is append operation\n","This will write on next line"])
# f1.write("Ashish")

# Manual way to read file using loop :
# f1 = open("file1.txt","r")

# for data in f1:
#     print(data)

# print(f1.read())  # This will not print unwanted extra lines

# print(f1.readline(1))  # this will return one character

# print(f1.readlines(0))  # this will return one line in form of list


# tell() and seek() :

# print(f1.tell())   # this will return current location of file pointer
# print(f1.readline())
# print(f1.readline())
# print(f1.readline())
# print(f1.readline())
# print(f1.readline())
# print(f1.tell())
# print(f1.seek(7)) # this will shift pointer location to given number
# print(f1.readline())
# print(f1.readline())
# print(f1.tell())

# f1.close()   # always close file to avoid differnt output and errors (this can be done in finally block of exception)

# with block : This will close file automatically

# with open("file1.txt","r") as f1:
#     print(f1.read())

# we can copy any file easily

# with open("file1.txt",'r') as f1, open("file2.txt","w") as f2:
#     f2.write(f1.read())

# Serialization and Deserialization :

# In file handling by default only string is allowed for read and write operation
# 
# Serialization => object --> btye
# Deserialization => byte --> object

import pickle

# load(read) , dump(write)

li1 = ["Ashish",23]

# "wb" and "rb"  -> for byte mode

# f1 = open("file1.txt",'wb')
# # f1.write(li1)   # TypeError: a bytes-like object is required, not 'list'

# pickle.dump(li1,f1)
# f1.close()

# f1 = open("file1.txt","rb")
# print(pickle.load(f1))

class Person:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name} {self.age}"

p1 = Person("Ashish",23)

with open("file1.txt","wb") as f1:
    pickle.dump(p1,f1)

with open("file1.txt", "rb") as f2:
    print(pickle.load(f2))





