# 7.	Write a program to check whether a year is a leap year.

print("Enter a year : ", end = "")
year = int(input())
if year%4 ==0:
    print(f"Yes, {year} is a Leap year")
else:
    print("No, It's not a leap year")