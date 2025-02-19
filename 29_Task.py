# 29.	Write a function to check if a string is a palindrome.
def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Ignore case and spaces
    return s == s[::-1]

print(is_palindrome("racecar"))  # Example usage
