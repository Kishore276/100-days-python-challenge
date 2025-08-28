while True:
    num = chr(input("Enter a number: "))

    if num > 0:
        print("It is a Positive Number")
    elif num < 0:
        print("It is a Negative Number")
    else:
        print("Zero is neither positive nor Negetive")

    cont = input("Do you want to continue? (yes/no): ")
    if cont.lower() != "yes":
        break