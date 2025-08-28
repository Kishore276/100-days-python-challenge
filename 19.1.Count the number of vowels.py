import re

def count_vowels(s):
    return len(re.findall('[aeiouAEIOU]', s))

# Test the function
s = input("Enter a string: ")
print("Number of vowels:", count_vowels(s))