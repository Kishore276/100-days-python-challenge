def sum_odd_position_digits(num):
    num_str = str(num)
    total = 0

    for i in range(0, len(num_str), 2):  # Start from index 0 and step by 2
        total += int(num_str[i])

    return total
number = int(input("Enter a number: "))
print(f"Sum of digits at odd positions: {sum_odd_position_digits(number)}")
