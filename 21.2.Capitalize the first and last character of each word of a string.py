s = "acm code sprint"
result = ' '.join(word[0].upper() + word[1:-1] + word[-1].upper() if len(word) > 1 else word.upper() for word in s.split())
print(result)  # Output: "HeLlo WoRlD ThIs Is A TeSt"