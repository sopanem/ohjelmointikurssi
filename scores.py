def main():
    file_name = input("Enter the name of the score file: ")
    people = {}
    with open(file_name, "r") as file:
        for line in file.readlines():
            line = line.split()
            people[line[0]] = people.get(line[0], 0) + int(line[1])
    print("Contestant score:")
    for person in sorted(people):
        print(f"{person} {people[person]}")


if __name__ == "__main__":
    main()
