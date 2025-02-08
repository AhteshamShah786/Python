# 11.	Write a program to display the multiplication table of a number entered by the user.

number = int(input("Enter a number to display its multiplication table: "))

print(f"Multiplication table of {number}:")
for i in range(1, 11):  
    print(f"{number} x {i} = {number * i}")