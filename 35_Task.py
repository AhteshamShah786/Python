#35 Write a Python program to count the number of occurrences of each character in a given string.

def char_count(string):
    counts = {}
    for char in string:
        counts[char] = counts.get(char, 0) + 1
    return counts

string = "hello world"
print(char_count(string))
