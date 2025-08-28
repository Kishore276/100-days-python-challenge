def fibonacci(n):
    fib = [0, 1]
    for i in range(2, 10):  # We only need Fibonacci numbers for digits 0-9
        fib.append(fib[-1] + fib[-2])
    return fib
def replace_digits_with_fibonacci(num):
    fib_map = fibonacci(10)
    return ''.join(str(fib_map[int(digit)]) for digit in str(num))
num = int(input("Enter a number: "))
print(replace_digits_with_fibonacci(num))
