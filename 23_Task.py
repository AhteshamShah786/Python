# 23.	Write a program to check if a string is a palindrome.
text = input("Enter a string: ").lower().replace(" ", "")  # Convert to lowercase and remove spaces
if text == text[::-1]:  # Check if reversed string is equal to original
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
