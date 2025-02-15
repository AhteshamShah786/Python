# 19.	Write a program to count how many times a specific number appears in a list.

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
target = int(input("Enter the number to count: "))

count = numbers.count(target)
print(f"The number {target} appears {count} times in the list.")
