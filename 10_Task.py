# 10.	Write a program to calculate the sum of numbers from 1 to n, where n is entered by the user.

number = int(input("Enter a number till which you want to print sum of numbers from 1 : "))
sum = 0
for i in range(1, number+1):
    sum+= i
print(sum)