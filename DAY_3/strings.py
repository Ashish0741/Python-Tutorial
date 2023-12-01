# Python supports only single line comment

str_single_quote = "Python"         # single quote
str_double_quote = 'Python'         # double quote
str_multi_line = '''                
Hello,
This is multi line string
'''

print(str_single_quote)
print(str_double_quote)
print(str_multi_line)

print(40 * "=")

# Indexing start from 0
# In python we have positive indexing from 0 and negative indexing from -1

print(str_single_quote[1])
print(str_single_quote[-1])

print(40 * "=")

# why both str_double_quote and str_double_quote[0] addresses are different ? 
# Ans : Due to different strings they have different memory addresses.

print(id(str_double_quote))
print(id(str_double_quote[0]))

print(40 * "=")

str1 = 'Fynd'
print(str1 + ' :' ,id(str1))
print(str1[0] + ' :' ,id(str1[0]))
print(str1[1] + ' :' ,id(str1[1]))
print(str1[2] + ' :' ,id(str1[2]))
print(str1[3] + ' :' ,id(str1[3]))

print(40 * "=")

# slicing
str_new = "SLICING"
print(str_new[:])
print(str_new[2:])
print(str_new[2:5])
print(str_new[::-1])
print(str_new[:5:2])

print(40 * "=")


# functions
print(len(str_new)) # here len is function
print(str_new.count('I')) # str_new is reference variable and count is method

print(40 * "=")




