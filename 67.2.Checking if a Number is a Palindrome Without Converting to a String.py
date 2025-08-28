def is_palindrome(n):
    """Check if a number is a palindrome without converting to a string."""
    if n < 0:
        return False
    original = n
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return original == reversed_num
number = 12321
result = is_palindrome(number)
print(f"The number {number} is a palindrome: {result}")