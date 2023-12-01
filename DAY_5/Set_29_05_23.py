
# Sets :

# 1. Mutable
# 2. Duplication not allowed
# 3. Unordered
# 4. Use curly brackets --> {}
# 5. every set is subset of itself

set1 = {1,2,3,4}
print(set1)

print(40 * '=')


set2 = {1,'hi',2.34}
print(set2)

print(40 * '=')


set3 = {1,2,3,2,4,3}
print(set3)

print(40 * '=')


# set4 = {[23,4,5,6]}  ----> not allowed in set
# print(set4)

# print(40 * '=')


set5 = {(23,4,5,6),4,5,6}
print(set5)

print(40 * '=')



# Methods :

set6 = {1,2,3,4,5}
set6.add(76)  
print(set6)

print(40 * '=')

set6.remove(3)  # remove using value
print(set6)

print(40 * '=')


# Math methods :

set11 = {1,2,3,4,5}
set12 = {1,2,6,7,8}

print(set11.intersection(set12))  # will give common element of set11 & set12

print(40 * '=')

print(set11.union(set12))  # will give all element in either set.

print(40 * '=')

print(set11.difference(set12))  # will give all elements of set11 except common element between set11 and set12

print(40 * '=')

print(set11.symmetric_difference(set12)) # opposite of intersection (except common element all will be return)

print(40 * '=')


# Using operators for above methods :

print("Intersection : ",set11 & set12)
print("Union : ",set11 | set12)
print("Difference : ",set11 - set12)
print("Symmetric Difference : ",set11 ^ set12)


set13 = {3,4,6,7,8}
print(set11 - set13.difference(set12))
