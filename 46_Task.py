# 46.	Write a program to find the second largest number in a list.

def second_largest(numbers):
    unique_numbers = list(set(numbers))  # Remove duplicates
    unique_numbers.sort(reverse=True)
    return unique_numbers[1] if len(unique_numbers) > 1 else None

print(second_largest([10, 20, 4, 45, 99, 99]))  
