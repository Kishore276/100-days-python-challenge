from collections import Counter

def letter_frequency(s):
    s = s.lower() 
    frequency = Counter(c for c in s if c.isalpha())  # Count only letters
    for letter, count in frequency.items():
        print(f"'{letter}': {count}")

string = input("Enter a string: ")
letter_frequency(string)
