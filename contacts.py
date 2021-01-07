import csv


def read_file(fileName):
    contacts = {}
    with open(fileName) as f:
        csvFile = csv.reader(f, delimiter=';')

        for row in csvFile:
            for col in row:
                print(col)


def main():
    info = read_file("contacts.csv")


if __name__ == "__main__":
    main()
