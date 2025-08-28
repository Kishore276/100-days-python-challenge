def is_palindrome(num):
    return str(num) == str(num)[::-1]
def count_palindromic_numbers(N):
    return sum(1 for num in range(1, N) if is_palindrome(num))
N = 100  
palindrome_count = count_palindromic_numbers(N)
print("Count of palindromic numbers:", palindrome_count)