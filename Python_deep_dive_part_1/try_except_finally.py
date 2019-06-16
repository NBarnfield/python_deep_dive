a = 1
b = 0

try:
    a = int(input("What is your first value?"))
except:
    print("{0} is not a valid integer".format(a))
finally:
    print('Your first value is {0}'.format(a))

try:
    b = int(input("What is your first value?"))
except:
    print("{0} is not a valid integer".format(b))
finally:
    print('Your first value is {0}'.format(b))

try:
    print(a/b)
except ZeroDivisionError:
    print("You cannot divide by zero!")
finally:
    print('This will always print!')