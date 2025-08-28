def nearest_power_of_2(n):
    """Find the nearest power of 2 greater than or equal to n."""
    if n <= 0:
        return 1  # The nearest power of 2 for non-positive numbers is 1
    power = 1
    while power < n:
        power *= 2
    return power
number = 20
result = nearest_power_of_2(number)
print(f"The nearest power of 2 greater than or equal to {number} is: {result}")