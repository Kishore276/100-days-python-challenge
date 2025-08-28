def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

# Ask the user for the term number
n = int(input("Enter the term number: "))

# Find and print the nth term in the Fibonacci series
nth_term = fibonacci(n)
print(f"The {n}th term in the Fibonacci series is: {nth_term}")
