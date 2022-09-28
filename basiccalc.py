import math

# Ask for 2 variable inputs
x = float(input('Create a Variable "x":'))
y = float(input('Create a Variable "y":'))

# Ask for operator type
request = str(input('Would you like to add, subtract, divide, or multiply?:'))

# Add
if request == 'add':
    print(x, '+', y, '=', x + y)

# Subtract
elif request == 'subtract':
    print(x, '-', y, '=', x - y)

# Divide
elif request == 'divide':
    remainderval = round(x % y, 2)
    print(x, '/', y, '=', int(x // y),'with a remainder of', remainderval)

# Multipy
elif request == 'multiply':
    print(x, '*', y, '=', x * y)

# Handle Invalid Requests
else:
    print('invalid request')
