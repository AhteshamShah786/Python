# 6.	Write a program to find the largest of three numbers

num1 = 5
num2 = 2
num3 = 6
print(f"There are three numbers: {num1},{num2},{num3}")
if (num1>num2) & (num1>num3):
    print(f"{num1} is the largest number")
elif (num2>num1) & (num2>num3):
    print(f"{num2} is the largest number")
elif (num3>num1) & (num3>num2):
    print(f"{num3} is the largest number")