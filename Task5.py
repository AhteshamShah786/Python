# 5.	Write a program to check whether a number is even or odd.

print("Enter a number to check whether it is even or odd : ", end = "")
num = int(input())
if num%2 == 0:
    print(f"{num} is EVEN number")
elif num%2 !=0:
    print(f"{num} is ODD number")