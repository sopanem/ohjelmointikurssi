"""
The first example of a home made class.
"""


class Person:

    def __init__(self, name, initial_money, addr):

        self.__name = name
        self.__money = initial_money
        self.__addr = addr

    def printout(self):

        print("—" * 25)
        print("Name:   ", self.__name)
        print("Wealth: ", self.__money)
        print("Address:", self.__addr)

    def add_money(self, amount):

        if amount < 0.0:
            return False
        else:
            self.__money += amount
            return True

    def make_payment(self, price):

        if price < 0.0:
            print("The price can't be negative.")
        elif price > self.__money:
            print("You can't afford that.")
        else:
            self.__money -= price

    def move(self, new_addr):
        self.__addr = new_addr


def main():

    denzil = Person("Denzil Dexter", 100.00, "320 Memorial Dr.")

    denzil.printout()

    denzil.move("20 Chestnut St.")

    denzil.printout()


if __name__ == "__main__":
    main()
