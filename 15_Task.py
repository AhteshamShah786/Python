# 15.	Write a program to take 5 numbers as input from the user, store them in a list, and display the list
numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("The list of numbers:", numbers)
