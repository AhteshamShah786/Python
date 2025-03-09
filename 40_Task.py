# 40.	Write a program to simulate a simple calculator with options for addition, subtraction, multiplication, and division.

def calculator():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    operation = input("Choose operation (+, -, *, /): ")

    if operation == '+':
        print("Result:", a + b)
    elif operation == '-':
        print("Result:", a - b)
    elif operation == '*':
        print("Result:", a * b)
    elif operation == '/':
        if b != 0:
            print("Result:", a / b)
        else:
            print("Error! Division by zero.")
    else:
        print("Invalid operation!")

calculator()
