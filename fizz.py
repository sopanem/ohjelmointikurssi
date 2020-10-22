i = int(input("How many numbers would you like to have? "))

for n in range(1, i+1):
    if n % 7 == 0 and n % 3 == 0:
        print("zip boing")
    elif n % 3 == 0:
        print("zip")
    elif n % 7 == 0:
        print("boing")
    else:
        print(n)
