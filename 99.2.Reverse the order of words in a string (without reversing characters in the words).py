def reverse_words(sentence):
    words = sentence.strip().split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

# Example usage
text = "Python is very powerful"
result = reverse_words(text)
print("Reversed words:", result)
