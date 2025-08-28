def is_palindrome(s):
    """
    Check if a given string is a palindrome using a loop.

    Args:
        s (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    i, j = 0, len(s) - 1
    while i < j:
        if s[i]!= s[j]:
            return False
        i += 1
        j -= 1
    return True

# Example usage:
string = input("Enter a string: ")
if is_palindrome(string):
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")