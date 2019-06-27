# Creating an integer object we can see its memory reference.
c = 20
hex(id(c))
type(c)

# Both objects will point to the same memory address - they will not create a new reference!
c = 10
d = 10
hex(id(c))
hex(id(d))