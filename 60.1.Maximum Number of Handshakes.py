def max_handshakes(n):
    if n < 2:
        return 0 
    return n * (n - 1) // 2
n = 5 
handshakes = max_handshakes(n)
print(f"The maximum number of handshakes among {n} people is: {handshakes}")