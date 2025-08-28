def replace_vowels(s):
    vowels = {'a': 'u', 'e': 'a', 'i': 'e', 'o': 'i', 'u': 'o',
              'A': 'U', 'E': 'A', 'I': 'E', 'O': 'I', 'U': 'O'}
    return ''.join(vowels[char] if char in vowels else char for char in s)
s = "Hello World"
print(replace_vowels(s))
