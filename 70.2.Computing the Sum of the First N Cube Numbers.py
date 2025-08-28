def sum_of_cubes(N):
    return sum(i**3 for i in range(1, N + 1))
N = 5
print(sum_of_cubes(N))