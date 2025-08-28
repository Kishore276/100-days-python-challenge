def reverse_each_word(text):
    return ' '.join(word[::-1] for word in text.split())
string = "ACM Code Sprint 100"
print("Reversed words:", reverse_each_word(string))
