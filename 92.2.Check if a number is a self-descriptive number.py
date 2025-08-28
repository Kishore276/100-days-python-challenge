def is_self_descriptive(num):
    num_str = str(num)
    length = len(num_str)

    for i in range(length):
        count = num_str.count(str(i))
        if int(num_str[i]) != count:
            return False
    return True
number = int(input("Enter a number: "))
if is_self_descriptive(number):
    print(f"{number} is a self-descriptive number.")
else:
    print(f"{number} is not a self-descriptive number.")
