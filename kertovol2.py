i = int(input("Choose a number: "))
run = True

tot = 0
f = 1
while not tot > 100:

    tot = f*i
    print(f"{f} * {i} = {tot}")
    f += 1
