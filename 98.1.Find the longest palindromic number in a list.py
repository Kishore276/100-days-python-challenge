def is_palindrome(n):
    return str(n) == str(n)[::-1]
def longest_palindromic_number(num_list):
    palindromes = [n for n in num_list if is_palindrome(n)]
    if not palindromes:
        return None
    return max(palindromes, key=lambda x: len(str(x)))
numbers = [121, 90909, 12321, 456, 888888, 999]
print("Longest palindromic number:", longest_palindromic_number(numbers))
