# a is a dynamic reference to an object in memory
# When a new value is assigned to it the reference changes to a separate address with a new type
a = 'hello'
# This is type of the object that A is referencing
# Each object will therefore show a different memory id and type
print(type(a))
print(hex(id(a)))
a = 10
print(type(a))
print(hex(id(a)))
a = lambda x: x**2
print(a(2))
print(type(a))
print(hex(id(a)))
a = 3 + 4j
print(type(a))
print(hex(id(a)))
