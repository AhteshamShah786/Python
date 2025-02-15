# 16.	Write a program to calculate the sum and average of elements in a list.

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
total = sum(numbers)
average = total / len(numbers)

print("Sum:", total)
print("Average:", average)
