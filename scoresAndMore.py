def main():
    file_name = input("Enter the name of the score file: ")
    people = {}
    try:
        file = open(file_name, "r")

        for original_line in file.readlines():
            line = original_line.split()
            if len(line) != 2:
                print("There was an erroneous line in the file:")
                print(original_line, end="")
                exit()
            if not line[1].isdigit():
                print("There was an erroneous score in the file:")
                print(line[1])
                exit()
            people[line[0]] = people.get(line[0], 0) + int(line[1])

        print("Contestant score:")
        for person in sorted(people):
            print(f"{person} {people[person]}")
    except Exception:
        print("There was an error in reading the file.")


if __name__ == "__main__":
    main()
