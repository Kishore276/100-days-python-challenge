def remove_vowels(s):
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in s if char not in vowels])

s = " Remove the vowels from a String"
print("Original string:", s)
print("String without vowels:", remove_vowels(s))