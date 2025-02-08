# 11.	Write a program to display the multiplication table of a number entered by the user.

number = int(input("Enter a number for which you want to print a table : "))
for i in range(1,11):
    print(f"{i} * {number} = {i*number}")