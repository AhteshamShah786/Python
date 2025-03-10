# 41.	Write a program to count the occurrences of each character in a string

def char_count(s):
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    return counts

print(char_count("hello world"))

