def to_camel_case(sentence):
    words = sentence.split()
    if not words:
        return ""
    return words[0].lower() + ''.join(word.capitalize() for word in words[1:])
sentence = input("Enter a sentence: ")
print(to_camel_case(sentence))
