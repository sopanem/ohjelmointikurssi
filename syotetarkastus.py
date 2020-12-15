"""
COMP.CS.100 Programming 1
Print a box with input error checking
"""


def read_input(text_of_input):
    invalid = True
    while invalid:
        try:
            lenght = int(input(text_of_input))
            if lenght > 0:
                invalid = False
        except ValueError:
            pass

    return lenght

def print_box(w, h, m):
    for counter in range(0, h):
        print(w * m)


def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
