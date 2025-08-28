def count_divisible(N, X, Y):
    count_X = (N - 1) // X
    count_Y = (N - 1) // Y
    count_XY = (N - 1) // (X * Y)
    return count_X + count_Y - count_XY
N = 20  
X = 3 
Y = 5  
result = count_divisible(N, X, Y)
print(result)