def xor_range(L, R):
    def xor_upto(n):
        if n % 4 == 0:
            return n
        elif n % 4 == 1:
            return 1
        elif n % 4 == 2:
            return n + 1
        else:
            return 0
    return xor_upto(R) ^ xor_upto(L - 1)
print(xor_range(3, 9))