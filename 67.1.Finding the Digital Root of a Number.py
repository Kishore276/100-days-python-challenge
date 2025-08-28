def digital_root(n):
    """Calculate the digital root of a number."""
    if n == 0:
        return 0
    return 1 + (n - 1) % 9
number = 9875
result = digital_root(number)
print(f"The digital root of {number} is: {result}")