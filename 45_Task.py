# 45.	Write a program to calculate the sum of digits of a given number.

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

print(sum_of_digits(1234))  
