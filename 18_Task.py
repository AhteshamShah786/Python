# 18.	Write a program to reverse a list.
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
reversed_list = numbers[::-1]

print("Reversed list:", reversed_list)
