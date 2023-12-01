
# Dictionary :

# 1. Mutable
# 2. In dictionary we store all things in key value pair
# 3. Indexing does not work in dictionary
# 4. Use curly brackets {}

# Creation :

dic1 = {}
print(dic1)

print(40 * '=')

dic2 = {1:200, 2:300, 3:600}
print(dic2)

print(id(dic2))
print(id(dic2[1]))

print(40 * '=')

dic3 = {1:34, "key":200}
print(dic3)

print(40 * '=')

dic4 = {3.14:500}
print(dic4)

print(40 * '=')

# dic5 = {[2,3,4]:"list"}  --> mutable type cannot be key in dictionary
# print(dic5)

dic6 = {(2,4,6):"tuple"}
print(dic6)


print(40 * '=')

dic7 = {1:[2,3,5,6,7]}
print(dic7)

print(40 * '=')

dic8 = {2:(45,678,9)}
print(dic8)

print(40 * '=')

dic9 = {1:{"inner_key":"inner_value"}}
print(dic9)

print(id(dic9[1]))
print(id(dic9[1]["inner_key"]))

print(40 * '=')

dic10 = {1:300, 1:500, 1:700}  # This will overwrite the value of key 1 due to same key
print(dic10)

print(40 * '=')

# Accessing (we can access any value only by key):

print(dic2[2])
print(dic4[3.14])
print(dic6[(2,4,6)])
print(dic7[1][0])
print(dic8[2][-1])
print(dic9[1]["inner_key"])  # this is called chaining ---> avoid usage of chaining as this consumes time


print(40 * '=')

# Key value methods :

dic11 = {1:34, "key":"value",(23,67):600}

print(dic11.keys())

print(40 * '=')

print(dic11.values())

print(id(dic11))

print(40 * '=')

# Insertion or Updation :

dic11.update({4:"update"})  # will update whole dictionary ---> adding new key value pair
print(dic11)

print(id(dic11))

print(40 * '=')

# dic11[7] = 567  --> avoid this type addition of new pair
# print(dic11)

# print(40 * '=')

dic11[1] = 89  # will update existing value of key 1
print(dic11)

print(40 * '=')

# dic11.update({1,678})  --> avoid this type updation of existing pair
# print(dic11)


# Deletion :

dic11.pop('key')  # used to delete pair using key
print(dic11)

print(40 * '=')

dic11.popitem()  # will delete unknown item
print(dic11)

print(40 * '=')







