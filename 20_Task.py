# 20.	Write a program to sort a list in ascending order.

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
sorted_list = sorted(numbers)

print("Sorted list:", sorted_list)
