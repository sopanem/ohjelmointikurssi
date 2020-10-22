run = True

i = input("Answer Y or N: ")
while run:
    if i == "y" or i == "Y":
        print(f"You answered {i}")
        run = False
    elif i == "n" or i == "N":
        print(f"You answered {i}")
        run = False
    else:

        print("Incorrect entry.")
        i = input("Please retry: ")
