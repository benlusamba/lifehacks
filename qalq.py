# Calculator with user inputs

#User inpiuts for numbers a, b and operation
a = input("first number: ")
operation = input('operation: ')
b = input("second number number: ")

#convert numerical inputs to integers to enable calculations:
x = int(a)
y = int(b)

#define calc function:
def calc(x, y, operation):
    if operation == '+':
        return x + y
    elif operation == '-':
        return x - y
    elif operation == '*':
        return x * y
    elif operation == '/':
        return x / y
    elif operation == '^':
        return x ** y

result = calc(x,y,operation)
print(result)
