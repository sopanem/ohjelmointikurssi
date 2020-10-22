run = True

i = input("Bored? (y/n) ")
while run:

    if i == "y" or i == "Y":
        print("Well, let's stop this, then.")
        run = False
    elif i == "n" or i == "N":
        i = input("Bored? (y/n) ")
        run = True
    else:

        print("Incorrect entry.")
        i = input("Please retry: ")

