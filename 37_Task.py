#37 Write a Python program to reverse each word in a given string while maintaining the word order.

def reverse_words(sentence):
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)

sentence = "hello world python programming"
print(reverse_words(sentence))
