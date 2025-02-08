# 12.	Write a program to count the number of vowels in a string.
myString = input("Enter any string to check how many vowels are present in it :")
count = 0
myString = myString.lower()
for char in myString:
    if char in "aeiou":
        count+= 1
print(f"Total number of vowels in string are : {count}") 