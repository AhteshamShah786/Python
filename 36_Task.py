#36 Write a Python program to find the longest word in a given string.

def longest_word(sentence):
    words = sentence.split()
    longest = max(words, key=len)
    return longest

sentence = "apple banana strawberry orange"
print("Longest word:", longest_word(sentence))
