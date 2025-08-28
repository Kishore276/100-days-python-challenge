from collections import Counter

def char_frequency(s):
    return Counter(s)

# Test the function
s = "acmcodesprint100"
print(char_frequency(s))