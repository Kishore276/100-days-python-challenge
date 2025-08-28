def count_decodes(digits):
    n = len(digits)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        if digits[i - 1] != '0':
            dp[i] += dp[i - 1]
        if i > 1 and (digits[i - 2] == '1' or (digits[i - 2] == '2' and digits[i - 1] <= '6')):
            dp[i] += dp[i - 2]
    return dp[n]
digits = "121"
print(count_decodes(digits)) 