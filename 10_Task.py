# 10.	Write a program to calculate the sum of numbers from 1 to n, where n is entered by the user
n = int(input("Enter a number to calculate the sum from 1 to n: "))
sum = 0

for i in range(1, n + 1):
    sum += i  

print(f"The sum of numbers from 1 to {n} is {sum}")