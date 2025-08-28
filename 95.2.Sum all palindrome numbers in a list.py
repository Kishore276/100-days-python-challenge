def is_palindrome(n):
    return str(n) == str(n)[::-1]
def sum_of_palindromes(numbers):
    return sum(n for n in numbers if is_palindrome(n))
num_list = [121, 131, 123, 44, 55, 234]
print("Sum of palindromes:", sum_of_palindromes(num_list))
