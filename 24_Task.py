# 24.	Write a program to count the number of words, vowels, and consonants in a string.
text = input("Enter a string: ").lower()
words = text.split()
vowels = "aeiou"
vowel_count = sum(1 for char in text if char in vowels)
consonant_count = sum(1 for char in text if char.isalpha() and char not in vowels)

print("Number of words:", len(words))
print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)
