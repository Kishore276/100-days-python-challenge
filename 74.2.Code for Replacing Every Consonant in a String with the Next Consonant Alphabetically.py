def replace_consonants(s):
    consonants = "bcdfghjklmnpqrstvwxyz"
    next_consonant = {c: consonants[(i + 1) % len(consonants)] for i, c in enumerate(consonants)}
    return ''.join(next_consonant[c] if c in next_consonant else c for c in s)
print(replace_consonants("hello world"))