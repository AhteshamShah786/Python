# 34.	Write a program to count the number of occurrences of each word in a given string.

def word_count(sentence):
    words = sentence.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

sentence = "apple banana apple orange banana apple"
print(word_count(sentence))
