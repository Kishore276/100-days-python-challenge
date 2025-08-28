def harmonic_mean(numbers):
    n = len(numbers)
    if n == 0:
        return 0
    reciprocal_sum = sum(1 / x for x in numbers if x != 0)
    if reciprocal_sum == 0:
        return 0
    return n / reciprocal_sum
numbers = [1, 2, 4, 8]
print("Harmonic Mean:", harmonic_mean(numbers))
