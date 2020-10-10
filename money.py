price = int(input("Purchase price: "))
amount_of_money = int(input("Paid amount of money: "))

tmp = amount_of_money - price

if tmp <= 0:
    print("No change")
else:
    print("Offer change:")

    for i in [10, 5, 2, 1]:
        (tmp2, tmp) = divmod(tmp, i)
        if tmp2 != 0:
            if i == 5:
                print(str(tmp2) + " five-euro notes")
            elif i == 10:
                print(str(tmp2) + " ten-euro notes")
            elif i == 1:
                print(str(tmp2) + " one-euro coins")
            elif i == 2:
                print(str(tmp2) + " two-euro coins")
