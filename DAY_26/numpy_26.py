
# ==============================================================
# Why to use NumPy :

# 1. Provides efficient storage
# 2. Provides better ways of handling data for processing
# 3. It is fast
# 4. Uses relatively less memory to store data

# ==============================================================ßß

import numpy as np

# creating simple numpy array

myarr = np.array([3,3,4,5,55])
print(myarr)

# defining type reference

arr1 = np.array([34,5,6,7,8],np.int8)
print(arr1)

# The conversion of 68888888 to int8 will fail in the future.
# for above issue will use proper type reference 
# np.int8
# np.int16
# np.int32
# np.int64
# np.int128
# np.int256

arr1 = np.array([34,5,68888888,7,8],np.int64)
print(arr1)


# Accessing array element

# print(arr1[0,1])  --> This will througj error as we are using 1D array and accessing in 2D form

print(arr1[0])  # 34

arr1 = np.array([[34,5,68888888,7,8]])

print(arr1[0,1])   # 5

# get shape of array

print(arr1.shape)   # (1, 5) --> (row, col)

# get type reference

print(arr1.dtype)  # int64

# changing particular matrix element

arr1[0,2] = 4

print(arr1)  # [[34  5  4  7  8]]

print(40 * '=')

# various ways to create numpy array :

# 1. Conversion from other python structures :

arr1 = np.array([[34,5,7], [45,6,9], [2,4,1]])

print("2D array : \n",arr1)

print(f"shape of arr1 : {arr1.shape}")

print(f"type reference of arr1 : {arr1.dtype}")

print(f"size of arr1 : {arr1.size}")

print(40 * '=')

# 2. Intrinsic numpy array creation :

zeros = np.zeros((2,5))  # it takes shape (row,col)

# by default it will create all element in float
print(zeros)

print(zeros.shape)

print(zeros.dtype)

# ----------------------------------------------------------

rng = np.arange(20)

print(rng)   # provides n number of array 

# ------------------------------------------------------------

# This will provide array with equally divide elments

lspace = np.linspace(1,5,4)  # (start,end,no. of elements)

print(lspace)

# ---------------------------------------------------------------

# Empty array :

mpty = np.empty((4,4))   # this will create array with random value

print(mpty)   

mpty_like = np.empty_like(lspace)  # this will create copy of passed array

print(mpty_like) 

ide = np.identity(10) # this will create identitical matrix of size (10x10)

print(ide)

print(ide.shape)
 
# ------------------------------------------------------------------------------

arr = np.arange(9)

print(arr)

arr = arr.reshape(3,3)  # used to reshape array

print(arr)

arr = arr.ravel()

print("array : ",arr,"shape : ",arr.shape)


# ----------------------------------------------------------------------------------

# Axis :

# In numpy axis starts with 0

# 1D : axis0
# 2D : axis0, axis1

# NOTE  : number of axis depends on array 

arr_new = np.array([[1,9,3], [3,490,589], [4,56,6]])

print(arr_new)

print("sum of axis 0 : ",arr_new.sum(axis=0))   # will give sum of all columns

print("sum of axis 1 : ",arr_new.sum(axis=1))   # will give sum of all rows

# Transpose of array

print(arr_new.T)

# to loop over 2D array

for num in arr_new.flat:
    print(num,end=" ")

print()

# to check dimension :

print("Dimension of arry : ",arr_new.ndim)

print("total bytes consumed : ",arr_new.nbytes)   # total bytes consumed

# to get index of max elemet :

print("index of max element : ",arr_new.argmax())

# to get index of min elemet :

print("index of min element : ",arr_new.argmin())

# to get index of arry in sorted manner :

print("index of arry in sorted manner : \n",arr_new.argsort())

# using above methods for axis :

print(arr_new)

print("index of arry in sorted manner : \n",arr_new.argsort(axis=0))

# -------------------------------------------------------------------------

# Mathematical operations :

arr2 = arr_new.T

print(arr_new)
print(arr2)

print("Addition of matrix : \n",arr2 + arr_new)

print("Subtraction of matrix : \n",arr2 - arr_new)

print("Multiplication of matrix : \n",arr2 * arr_new)

print("Division of matrix : \n",arr2 // arr_new)

# --------------------------------------------------------------

# to find number :

# print(arr2)

print(np.where(arr2>10))  # will give all indexs where condition mets 

# output : (array([1, 1, 2]), array([1, 2, 1]))

print(np.nonzero(arr2))  # this will return all indexes which are non-zero

# output : (array([0, 0, 0, 1, 1, 1, 2, 2, 2]), array([0, 1, 2, 0, 1, 2, 0, 1, 2]))

# ------------------------------------------------------------------

import sys

# storage review :

lis1 = [3,4,324,234,5]

arr_s = np.array(lis1)

print("Size of list : ",sys.getsizeof(1) * len(lis1))

print("size of numpy array : ",arr_s.itemsize * arr_s.size)

print(arr_s.flags)   # Information about the memory layout of the array.

print(arr_s.imag)   # imaginary part of array

# print(arr_s.dumps())  this will dump array & return string

# arr_s.dump("DAY_26/array.txt")  This will write the array in file 

print(arr_new.diagonal()) # this will return diagonal of matrix

arr_new.fill(6)  # this will fill array with given value & will take only int value

print(arr_new)








