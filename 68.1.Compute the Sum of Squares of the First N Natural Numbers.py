def sum_of_squares(n):
    """Compute the sum of squares of the first N natural numbers."""
    return (n * (n + 1) * (2 * n + 1)) // 6
N = 5
result = sum_of_squares(N)
print(f"The sum of squares of the first {N} natural numbers is: {result}")