def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b

def multiply(a, b):
    return a * b

a = int(input('Enter a number: '))
b = int(input('Enter a second number: '))
operation = input('Enter either add, sub, mult, or div: ')

if operation == 'add':
    print(add(a, b))
elif operation == 'sub':
    print(subtract(a, b))
elif operation == 'div':
    print(divide(a, b))
elif operation == 'mult':
    print(multiply(a, b))
else:
    print('user input error')