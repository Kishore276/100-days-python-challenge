def pell_sequence(n):
    pell = [0, 1]
    for i in range(2, n):
        pell.append(2 * pell[i - 1] + pell[i - 2])
    return pell[:n]
N = int(input("Enter the number of terms: "))
print(pell_sequence(N))
