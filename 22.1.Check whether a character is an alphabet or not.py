def is_alphabet(char):
    return char.isalpha()

char = input("Enter a character: ")

if is_alphabet(char):
    print(f"{char} is an alphabet.")
else:
    print(f"{char} is not an alphabet.")