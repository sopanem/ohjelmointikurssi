
import math


def lottery_probability(n, p):
    return int(math.factorial(n) / (math.factorial(n - p) * math.factorial(p)))


def ask_stuff():
    balls = int(input("Enter the total number of lottery balls: "))
    drawn = int(input("Enter the number of the drawn balls: "))

    if balls < 0:
        print("The number of balls must be a positive number.")
    elif drawn > balls:
        print("At most the total number of balls can be drawn.")
    else:
        print(
            f"The probability of guessing all {drawn} balls correctly is 1/{lottery_probability(balls, drawn)}")


def main():
    ask_stuff()


if __name__ == '__main__':
    main()
