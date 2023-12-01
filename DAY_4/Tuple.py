# Tuple :

# 1. Immutable
# 2. Cannot perfrom IUD operations
# 2. Duplicates are allowed
# 3. Use round brackets ()

tuple_1 = ()   # empty tuple
print(tuple_1)

print(40 * '=')

tuple_1 = (1,2,3,4)  # homogeneous
print(tuple_1)

print(40 * '=')

tuple_1 = tuple((1,2,3,43))  # using tuple class
print(tuple_1)

print(40 * '=')

tuple_1 = (1,2,3.4,'hi')   # heterogeneous
print(tuple_1)

print(40 * '=')

tuple_1 = (1,2,3,(3,45,6),2)  # nested tuple
print(tuple_1)

print(id(tuple_1))
print(id(tuple_1[3]))

print(40 * '=')


# TypeError: 'tuple' object does not support item assignment
# tuple_1[2] = 4
# print(tuple_1)


# Methods :

print("Number of occurance of 2 : ",tuple_1.count(2))   # will give number of occurance of given element

print(40 * '=')

print("Index of element 2 : ",tuple_1.index(2))  # will give index of given element if element is duplicate ..will give 1st occurance index

print(40 * '=')

# ==================================================================================

tuple_inside_list = [1,2,(23,56),45]
del tuple_inside_list[0]
print("tuple_inside_list : ",tuple_inside_list)

# TypeError: 'int' object does not support item deletion
# del tuple_inside_list[2][0] 
# print(tuple_inside_list)

print(40 * '=')

list_inside_tuple = (1,4,5,[34,56,7])
list_inside_tuple[3][1] = 90
print("list_inside_tuple : ",list_inside_tuple)

# TypeError: 'tuple' object does not support item assignment
# list_inside_tuple[0] = 90
# print("list_inside_tuple : ",list_inside_tuple)

print(40 * '=')


# slicing

tuple_1 = (34,6,7,8)

print(tuple_1[:2])

print(40 * '=')

print(tuple_1[::-1])

print(40 * '=')


