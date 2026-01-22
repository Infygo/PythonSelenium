# python basics
# ----------------
# >> cant concatenate string and int together
# >> "{}{}".format() method
# type(a) method 

# print
print('hello world')

# No need of type variables
a = 1
b = 2.0
c = 3.25
print(a, b, c)
d, e, f = 4, 'hello', True
print(d, e, f)
Str = 'hello world'
print(Str)

# print(a+str) -- doesnt work as a & str are of str and int data types

# concantenation using + & ,
print("concatenate using comma", e, Str)
print("concatenate using + "+ e + Str)

# .format method
print("{} {}".format(a,Str))

# .type method
print(type(Str)) # <class 'str'>

