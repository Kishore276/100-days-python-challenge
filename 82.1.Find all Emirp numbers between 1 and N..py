def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def is_emirp(num):
    if is_prime(num):
        reversed_num = int(str(num)[::-1])
        return reversed_num != num and is_prime(reversed_num)
    return False
def find_emirps(N):
    return [num for num in range(1, N) if is_emirp(num)]
N = 100 
emirps = find_emirps(N)
print("Emirp numbers:", emirps)