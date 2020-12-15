def main():
    fileName = input("Enter the name of the file: ")
    try:
        with open(fileName, "r") as f:
            file = f.readlines()

            lineTmp = 0
            for lines in file:
                line = lines.rstrip()
                lineTmp += 1
                print(f"{lineTmp} {line}")
    except Exception:
        print("There was an error in reading the file.")


if __name__ == '__main__':
    main()
