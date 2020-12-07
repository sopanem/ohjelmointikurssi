def reverse_name(name):
    return (" ".join(reversed(name.split(",")))).strip()


def main():
    print(reverse_name("x,x,"))


if __name__ == "__main__":
    main()
