"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

This program models a character adventuring in a video game.
"""


class Character:
    def __init__(self, name, hp):
        self.__name = name
        self.__items = {}
        self.__hp = hp

    def give_item(self, item):
        if item in self.__items:
            self.__items[item] += 1
        else:
            self.__items[item] = 1

    def remove_item(self, item):
        if item in self.__items:
            self.__items[item] -= 1
            if self.__items[item] == 0:
                self.__items.pop(item)

    def printout(self):
        print("Name: " + self.__name)
        print(f"Hitpoints: {self.__hp}")
        if self.__items:
            for item in sorted(self.__items):
                print(f"  {self.__items[item]} {item}")
        else:
            print("  --nothing--")

    def get_name(self):
        return self.__name

    def has_item(self, item):
        return item in self.__items

    def how_many(self, item):
        if item in self.__items:
            return self.__items[item]
        else:
            return 0

    def pass_item(self, item, target):

        if not item in self.__items:
            return

        self.remove_item(item)
        target.give_item(item)

        # TODO: implementation of the method

    def attack(self, target, weapon):

        if not weapon in WEAPONS:
            print(f"Attack fails: unknown weapon \"{weapon}\".")
            return

        if not weapon in self.__items:
            print(
                f"Attack fails: {self.get_name()} doesn't have \"{weapon}\".")
            return

        if target.get_name() == self.get_name():
            print(f"Attack fails: {self.get_name()} can't attack him/herself.")
            return

        print(
            f"{self.get_name()} attacks {target.get_name()} delivering {WEAPONS[weapon]} damage.")

        target.__hp -= WEAPONS[weapon]

        if target.__hp <= 0:
            print(f"{self.get_name()} successfully defeats {target.get_name()}.")

    # TODO: the implementation of the method


WEAPONS = {
    # Weapon          Damage
    # --------------   ------
    "elephant gun":     15,
    "gun":               5,
    "light saber":      50,
    "sword":             7,
}


def main():
    conan = Character("Conan the Barbarian", 10)
    deadpool = Character("Deadpool", 45)

    # Testing the pass_item method

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        conan.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        deadpool.give_item(test_item)

    conan.pass_item("sword", deadpool)
    deadpool.pass_item("hero outfit", conan)
    conan.pass_item("sausage", deadpool)
    deadpool.pass_item("gun", conan)
    conan.pass_item("sausage", deadpool)
    deadpool.pass_item("gun", conan)

    print("-" * 5, "How are things after passing items around", "-" * 20)
    conan.printout()
    deadpool.printout()

    # Testing a fight i.e. the attack method

    print("-" * 5, "Let's see how a fight proceeds", "-" * 32)

    # Conan's turn
    conan.attack(deadpool, "sword")  # Conan doesn't have a sword.
    # A character is not allowed to attack himself.
    conan.attack(conan, "gun")
    # Pen is not a known weapon in WEAPONS dict.
    conan.attack(conan, "pen")
    conan.attack(deadpool, "gun")   # Attack with a gun.

    # Deadpool retaliates
    deadpool.attack(conan, "sword")  # Deadpool has a sword.

    # Conan's 2nd turn
    conan.attack(deadpool, "gun")   # Attack with a gun again.

    # Deadpool strikes back again and Conan drops "dead".
    deadpool.attack(conan, "sword")

    print("Are You Not Entertained?!")

    print("-" * 5, "How are things after beating each other up", "-" * 20)

    conan.printout()
    deadpool.printout()


if __name__ == "__main__":
    main()
