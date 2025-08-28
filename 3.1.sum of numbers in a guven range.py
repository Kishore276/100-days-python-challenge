def sum_of_numbers_in_range(start, end):
    n = end - start + 1
    return n * (start + end) // 2
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
result = sum_of_numbers_in_range(start, end)
print(f"The sum of numbers in the range [{start}, {end}] is: {result}")