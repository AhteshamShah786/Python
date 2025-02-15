# 17.	Write a program to find the largest and smallest elements in a list.

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

largest = max(numbers)
smallest = min(numbers)

print("Largest number:", largest)
print("Smallest number:", smallest)
