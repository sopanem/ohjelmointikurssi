"""
COMP.CS.100 Programming 1
Template Song: Old MacDonald
"""

def print_verse(animal, word):
    print("Old MACDONALD had a farm")
    print("E-I-E-I-O")
    print(f"And on his farm he had a {animal}")
    print("E-I-E-I-O")
    print(f"With a {word} {word} here")
    print(f"And a {word} {word} there")
    print(f"Here a {word}, there a {word}")
    print(f"Everywhere a {word} {word}")
    print("Old MacDonald had a farm")
    print("E-I-E-I-O")
    print("")

def main():
    print_verse("cow", "moo")
    print_verse("pig", "oink")
    print_verse("duck", "quack")
    print_verse("horse", "neigh")
    print_verse("lamb", "baa")


if __name__ == "__main__":
    main()
