def create_an_acronym(name):
    result = ""
    for n in name.split(" "):
        result += n[0].upper()
    return result


def main():
    create_an_acronym(name)


if __name__ == '__main__':
    main()
