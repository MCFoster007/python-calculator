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

operation = input("enter operation: ")
num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))

if operation == "+":
    result = add(num1, num2)
elif operation == "-":
    result = subtract(num1, num2)
elif operation == "*":
    result = multiply(num1, num2)
elif operation == "/":
    result = divide(num1, num2)
else:
    result = "invalid operation"

print(f"result: {result:.3f}")

