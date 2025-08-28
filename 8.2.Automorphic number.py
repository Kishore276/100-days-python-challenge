def is_automorphic(n):
   
    square = str(n ** 2)
    return square.endswith(str(n))

num = int(input("Enter a number: "))
if is_automorphic(num):
    print(f"{num} is an Automorphic Number.")
else:
    print(f"{num} is not an Automorphic Number.")