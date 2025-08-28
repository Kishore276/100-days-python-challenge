def capitalize_first_letter(sentence):
    result = ""
    capitalize_next = True
    for char in sentence:
        if char == " ":
            result += char
            capitalize_next = True
        elif capitalize_next:
            result += chr(ord(char) - 32) if 'a' <= char <= 'z' else char
            capitalize_next = False
        else:
            result += char
    return result

sentence = "this is a test sentence."
print(capitalize_first_letter(sentence))