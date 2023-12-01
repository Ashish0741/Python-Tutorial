# List :

# 1. Mutable
# 2. Can perform insert, update and delete operations
# 3. Duplicates are allowed
# 4. Use square brackets []

list_1 = []                # empty list
print("Empty List : ", list_1)

print(40 * "=")

# there are two ways to create list
# 1. using square brackets
# 2. using in-built list class

list_1 = [1, 2, 3, 4, 56]           # homogeneous
print("Homogeneous List : ", list_1)

print(40 * "=")

list_1 = list((1, 2, 3, 34, 54))
print("Using List class : ", list_1)

print(40 * "=")

list_1 = [1, 2, 3.14, "hello", 56]             # heterogeneous
print("Heterogeneous List : ", list_1)

print(40 * "=")

list_1 = [1, 2, [34, 67, 7], 4, 56]             # nested list
print("Nested List : ", list_1)

print(id(list_1))
print(id(list_1[2:]))

print(40 * "=")

# ==================================================================================

# Insertion :

list_1 = [1, 2, 3, 4, 56]
list_1.insert(0,99)   # this will insert 99 at 0th index 
print(list_1)

print(40 * "=")

list_1.insert(8,90)  # if we give index out of range it will insert at end of list
print(list_1)

print(40 * "=")

list_1.insert(-1,70)   # this will insert 70 at index + 1 i.e -2
print(list_1)

print(40 * "=")

# list_1.extend(100)  # error : extends works only for iterable element (having indexes)
# print(list_1)

# print(40 * "=")

list_1.extend([1,4,5])
print(list_1)

print(40 * "=")

# list_1.extend("hello")
# print(list_1)

# print(40 * "=")

list_1.append(100) # will add 100 at end of list
print(list_1)

print(40 * "=")

list_1.append([1,5,7]) # will add entire list as sublist at end of list
print(list_1)

print(40 * "=")


# ======================================================================================

# Updation : 

list_2 = [1, 2, 3, 4, 56]

list_2[0] = 4   # will update value of index 0
print(list_2)

print(40 * "=")


list_1[-1][0] = 78     # updating in nested list
print(list_1)


print(40 * "=")


# ======================================================================================

# Deletion :

list_2.remove(4)    # will delete given element and if duplicate elements are present then it will remove 1st occurance.
print(list_2)

print(40 * "=")

list_2.pop()   # will delete last element from list
print(list_2)


print(40 * "=")

list_2.pop(0)  # will delete given index element from list
print(list_2)

print(40 * "=")

list_1[-1].pop()   # will delete last element from nested list
print(list_1)

print(40 * "=")

list_2.clear()   # will empty the list 
print(list_2)

print(40 * "=")

del list_2  # will delete list from memory itself
# print(list_2)

print(40 * "=")

del list_1[-1]  # can delete single element too
print(list_1)

print(40 * "=")

# ======================================================================================

# Other Functions :

print("Occurance of 4 : ",list_1.count(4))

print(40 * "=")


# Shallow copy --> Pass by reference

list_1 = [1,2,65]
list_2 = [4,5,6]

print(list_1)
print(list_2)

# print(id(list_1))
# print(id(list_2))

print(40 * "=")

list_new = list_1    # This will not create new object ... list_new is referencing to list_1 that's why both lists will have same memory address
list_new[len(list_new)-1] = 567  # Due to above scenrio when we update 567 in list_new this will affect list_1 too.

print(list_1)
print(list_new)

print(id(list_1))
print(id(list_new))

print(40 * "=")


# Deep copy  --> Pass by value

list_1 = [1,2,65]
list_2 = [4,5,6]

print(list_1)
print(list_2)

# print(id(list_1))
# print(id(list_2))

print(40 * "=")

# There are two ways for deep copy
# 1. using copy method
# 2. using slicing

print("Using copy method : ")

list_new = list_1.copy()    # This will create new object ....
list_new[len(list_new)-1] = 567   # Due to above scenrio when we update 567 in list_new ... list_1 will not affect.

print(list_1)
print(list_new)

print(id(list_1))
print(id(list_new))

print(40 * "=")


print("Using slicing : ")

list_new = list_1[:]    # This will create new object ....
list_new[0] = 567   # Due to above scenrio when we update 567 in list_new ... list_1 will not affect.

print(list_1)
print(list_new)

print(40 * "=")


# Reverse method :

list_1.reverse() 
print("Reverse List : ",list_1)

print(40 * "=")

# list_1.append([12,3,6])
# list_1[-1].reverse() 
# print("Reverse List : ",list_1)

# print(40 * "=")

# sort method :

list_1.sort()  # will sort list in ascending order
print("Sort list in ascending order : ",list_1)

print(40 * "=")

list_1.sort(reverse=True)  # will sort list in descending order
print("Sort list in descending order : ",list_1)

print(40 * "=")



