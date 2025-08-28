def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]
def sum_of_digits_in_fibonacci(n):
    fib_nums = fibonacci(n)
    total_sum = sum(sum(int(digit) for digit in str(num)) for num in fib_nums)
    return total_sum
N = 10
print(f"Sum of digits of first {N} Fibonacci numbers:", sum_of_digits_in_fibonacci(N))
