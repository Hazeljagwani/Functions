def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

n1 = int(input("Type the first number"))
n2 = int(input("Type the second number"))

add(n1, n2)
print("The addition of these two numbers is ", add(n1, n2))

subtract(n1, n2)
print("The subtraction of these two numbers is ", subtract(n1, n2))

multiply(n1, n2)
print("The multiplication of these two numbers is ", multiply(n1, n2))

divide(n1, n2)
print("The division of these two numbers is ", divide(n1, n2))