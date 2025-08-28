def divisible_by_sum_of_squares(N):
    result = []
    for num in range(1, N):
        digit_squares_sum = sum(int(digit) ** 2 for digit in str(num))
        if num % digit_squares_sum == 0:
            result.append(num)
    return result
N = 100
print(divisible_by_sum_of_squares(N))