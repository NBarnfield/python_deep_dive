# Lists are mutable
my_list = [1, 2, 3]
type(my_list)
hex(id(my_list))
# The .append method appends to the current memory address
my_list.append(4)
hex(id(my_list))
my_list_1 = [1, 2, 3]
hex(id(my_list_1))
# Concatenated 2 objects - evaluates the right side, combines the two lists and then returns a new objects
my_list_1 = my_list_1 + [4]
hex(id(my_list_1))

# As are dictionaries
my_dict = dict(key1=1, key2='a')
my_dict
id(my_dict)
my_dict['key3'] = 10.5
my_dict
hex(id(my_dict))

# A tuple is immutable. It has its own memory address as does every element in it.
t = (1, 2, 3)
hex(id(t))
hex(id(t[0]))
hex(id(t[1]))
hex(id(t[2]))

# This will now have a different address as it is a different object
t = ([1, 2], 3, 4)
print(hex(id(t)))
print(hex(id(t[0])))
print(hex(id(t[1])))
print(hex(id(t[2])))

t[0].append(3)
print(hex(id(t)))
print(hex(id(t[0])))

# Despite an object being immutable it does not mean that the contents can't change.
# Particularly when dealing with collections.
