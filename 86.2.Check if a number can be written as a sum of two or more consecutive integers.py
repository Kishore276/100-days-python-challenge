def can_be_sum_of_consecutive(n):
    for start in range(1, n):
        sum_ = 0
        for num in range(start, n):
            sum_ += num
            if sum_ == n:
                return True
            if sum_ > n:
                break
    return False
num = int(input("Enter a number: "))
print(can_be_sum_of_consecutive(num))
