def is_vowel(char):
    char = char.lower()
    return char in 'aeiou'

def is_consonant(char):
    return char.isalpha() and not is_vowel(char)

char = input("Enter a character: ")

if is_vowel(char):
    print(f"{char} is a vowel.")
elif is_consonant(char):
    print(f"{char} is a consonant.")
else:
    print(f"{char} is neither a vowel nor a consonant.")