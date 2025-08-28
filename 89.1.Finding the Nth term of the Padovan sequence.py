def padovan(n):
    if n == 0 or n == 1 or n == 2:
        return 1
    p = [1, 1, 1]  # Initial three values
    for i in range(3, n + 1):
        p.append(p[i - 2] + p[i - 3])
    return p[n]
n = int(input("Enter the value of N: "))
print(f"The {n}th term of the Padovan sequence is: {padovan(n)}")
