def replace_word(s, old_word, new_word):
    words = s.split()
    new_words = [new_word if word == old_word else word for word in words]
    return ' '.join(new_words)

s = input("Enter a string: ")
old_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")

new_string = replace_word(s, old_word, new_word)
print("New string:", new_string)