#42 Write a program to check if a given string is a palindrome.

def is_palindrome(s):
    s = s.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    return s == s[::-1]

print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False
print(is_palindrome("A man a plan a canal Panama"))  # True
