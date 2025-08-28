def find_longest_word(sentence):
    words = sentence.split()
    longest_word = max(words, key=len) if words else ""
    return longest_word
sentence = "The quick brown fox jumped over the lazy dog"
print(f"The longest word in the sentence is: '{find_longest_word(sentence)}'")