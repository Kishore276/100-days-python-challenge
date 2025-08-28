def largest_lexicographical_permutation(s):
    return ''.join(sorted(s, reverse=True))
s = "abcde"  
result = largest_lexicographical_permutation(s)
print(result)