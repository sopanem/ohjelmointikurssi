def read_message():
    print("Enter rows of text. Quit by entering an empty row.")
    lines = ""
    i = 0
    while True:
        i += 1
        line = input()
        if line == "":
            break
        lines += f"{i} {line}\n"
    return lines


def main():
    file_name = input("Enter the name of the file: ")

    try:
        file = open(file_name, "w")
        file.write(read_message())
        print(f"File {file_name} has been written.")
    except Exception:
        print(f"Writing the file {file_name} was not successful.")


if __name__ == '__main__':
    main()
