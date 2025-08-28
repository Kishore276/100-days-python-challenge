def print_permutations(s):
    def permute(s, prefix=""):
        if len(s) == 0:
            print(prefix)
        else:
            for i in range(len(s)):
                remaining = s[:i] + s[i+1:]
                permute(remaining, prefix + s[i])

    permute(s)
s = "acm"
print_permutations(s)