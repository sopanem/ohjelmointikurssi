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

        # return self.return_string()

    def complement(self):
        return Fraction(-self.__numerator, self.__denominator)

    def reciprocal(self):
        return Fraction(self.__denominator, self.__numerator)

    def multiply(self, a):
        return Fraction(self.__numerator * a.__numerator, self.__denominator * a.__denominator)

    def divide(self, a):
        return Fraction(self.__numerator * a.__denominator, self.__denominator * a.__numerator)

    def add(self, a):
        return Fraction(self.__numerator * a.__denominator + a.__numerator * self.__denominator, self.__denominator * a.__denominator)

    def deduct(self, a):
        return Fraction(self.__numerator * a.__denominator - a.__numerator * self.__denominator, self.__denominator * a.__denominator)


def greatest_common_divisor(a, b):

    while b != 0:
        a, b = b, a % b

    return a
