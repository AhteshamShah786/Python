# 22.	Write a program to reverse a string without using slicing.
text = input("Enter a string: ")
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text  # Build the reversed string

print("Reversed string:", reversed_text)

# Another method:
# text = input("Enter a string: ")
# reversed_text = "".join(reversed(text))
# print("Reversed string:", reversed_text)
