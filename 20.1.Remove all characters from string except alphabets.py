def remove_non_alphabets(s):
    return ''.join([char for char in s if char.isalpha()])

s = "acm code sprint 100"
print("Original string:", s)
print("String with only alphabets:", remove_non_alphabets(s))