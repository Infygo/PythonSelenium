# Python data types
# List[] >mutable type >  similar to array list can hold elements of different data types
# List methods > append, insert, [-1] last value, [1:3], delete, len(list var),

# Tuple() > immutable type , similar to list but can't be modified / changed

# Dictionary > Key value pair > retrieve value by using the key


print('List data type')
values_list = [1, 2, "vig", 4, 5.0]
print(values_list)

# insert values_list to a list at an index position
values_list.insert(3, "rav")
print(values_list)

# last element of a list
print(values_list[-1])

# retrieve a specific range of elements
print(values_list[1:4]) # first index inclusive , last index excluding

# append values_list to the last index
values_list.append(6)
print(values_list)

# add element to an index position
values_list[2] = 3
print(values_list)

# length of an elements
print(len(values_list)) #7

# delete an element in list
del values_list[6]
print(values_list)
print('End of list data type')
print('-----------------------')

print('Tuple data type')
values_tuple = (1,2,3,4)
print(values_tuple[0])
# values_tuple[4] = 5 > tuple doesnt support item assigment / immutable
# print(values_tuple)
print('End of tuple data type')
print('-----------------------')

print('Dictionary data type')
values_dict = {'a':1, 'b':2, 'c':3, 4:'Hello'}
print(values_dict)
print(values_dict['a'])
print(values_dict[4])

info_dict = {}
info_dict["firstname"] = "vig"
info_dict["lastname"] = "rav"
info_dict["gender"] = 'Male'
print(info_dict)
