def is_palindrome(n):
    return str(n) == str(n)[::-1]
def count_palindromes_in_range(start, end):
    return sum(1 for i in range(start, end + 1) if is_palindrome(i))
start = 100
end = 200
print(f"Number of palindromes between {start} and {end}:", count_palindromes_in_range(start, end))
