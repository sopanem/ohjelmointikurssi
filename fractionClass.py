"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Fractions code template
"""


class Fraction:

    def __init__(self, numerator, denominator):

        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    def return_string(self):

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"

    def simplify(self):
        divisor = greatest_common_divisor(self.__denominator, self.__numerator)

        self.__denominator = int(self.__denominator / divisor)
        self.__numerator = int(self.__numerator / divisor)

        return self.return_string()


def greatest_common_divisor(a, b):

    while b != 0:
        a, b = b, a % b

    return a


def main():
    frac = Fraction()

    frac.return_string()
