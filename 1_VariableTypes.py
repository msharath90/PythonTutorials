# Variable Types in Python

a1 = 5
print(type(a1))
# <class 'int'>

a2 = 5.5
print(type(a2))
# <class 'float'>

a3 = 5+8j
print(type(a3))
# <class 'complex'>

a4 = [15, 60, 19]
print(type(a4))
print(a4)
# <class 'list'>
# [15, 60, 19]

a5 = {10, 20, 30, 10, 50, 30}
print(type(a5))
print(a5)
# <class 'set'>
# {10, 20, 50, 30} Might be varying, not fixed and all are unique

a6 = (20, 10, 20, 40)
print(type(a6))
print(a6)
# <class 'tuple'>
# (20, 10, 20, 40)

str1 = "sharath"
print(type(str1))
# <class 'str'>

st = 's'
print(type(st))
# <class 'str'> No Char type in python, both single and double code represents string

print(list(range(10)))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(range(2, 10, 2)))
# [2, 4, 6, 8]

print(list(range(10, 2, -2)))
# [10, 8, 6, 4]

print(type(range(10)))
# <class 'range'>

dict1 = {'sharath': 'python', 'akshay': 'Java', 'gaurav': 'C#'}
print(type(dict1))
# <class 'dict'>

print(dict1)
# {'sharath': 'python', 'akshay': 'Java', 'gaurav': 'C#'}

print(dict1.keys())
# dict_keys(['sharath', 'akshay', 'gaurav'])

print(dict1.values())
# dict_values(['python', 'Java', 'C#'])

print(dict1['akshay'])
# Java

print(dict1.get('gaurav'))
# C#
