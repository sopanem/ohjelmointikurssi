"""
Ohjelmointi 1 / Programming 1
Trangle's Area when the Sides Are Known
"""

from math import sqrt

def area(f,se,t):

    s = (f+se+t)/2
    return sqrt(s*(s-f)*(s-se)*(s-t))


def main():
    line = float(input("Enter the length of the first side: "))
    line1 = float(input("Enter the length of the second side: "))
    line2 = float(input("Enter the length of the third side: "))

    tot = area(line, line1, line2)
    print(f"The triangle's area is {round(tot, 1)}")


if __name__ == "__main__":
    main()
