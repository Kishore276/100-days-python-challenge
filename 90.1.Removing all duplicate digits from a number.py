def remove_duplicates(num):
    num_str = str(num)
    result = ""
    seen = set()

    for digit in num_str:
        if digit not in seen:
            result += digit
            seen.add(digit)

    return int(result)

number = int(input("Enter a number: "))
print(f"Number after removing duplicate digits: {remove_duplicates(number)}")
