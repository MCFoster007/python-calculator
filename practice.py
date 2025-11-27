print("let's practice python.")
name = input("what's your name? ")
print(f"nice to meet you, {name}!")
age = input("how old are you? ")
print(f"wow, {age} years old! that's great!")
print("welcome to the python calculator y'all!")
print(f"{name}, choose an operation: +, -, *, /")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "error: cannot divide by zero"
    return x / y

operation = input("Enter operation (+, -, *, /): ")
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
    
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = None
        print("Error: cannot divide by zero")
else:
    result = None
    print("Invalid operation")

if result is not None:
    print(f"result: {result:.3f} hours to study python!")





