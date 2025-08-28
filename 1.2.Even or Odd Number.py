while True:
    num = int(input("Enter a number: "))

    if num % 2 == 0:
        print(" It is an Even Number")
    else:
        print("It is a Odd Number")

    cont = input("Do you want to continue? (yes/no): ")
    if cont.lower()!= "yes":
        break