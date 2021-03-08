"""
COMP.CS.100 Programming 1
Read genres and tv-series from a file into a dict.
Print a list of the genres in alphabetical order
and list tv-series by given genre on user's command.
"""


def read_file(filename):
    series = {}

    try:
        file = open(filename, mode="r")

        for row in file:

            name, genres = row.rstrip().split(";")

            genres = genres.split(",")

            for genre in genres:
                series.setdefault(genre, []).append(name)

        file.close()
        return sorted(series.items())

    except ValueError:
        print("Error: rows were not in the format name;genres.")
        return None

    except IOError:
        print("Error: the file could not be read.")
        return None


def main():
    filename = input("Enter the name of the file: ")

    genre_data = read_file(filename)

    genre_text = ", ".join(genre_data)
    print(f"Available genres are: {genre_text}")

    while True:
        genre = input("> ")

        if genre == "exit":
            return

        for name, key in genre_data(genre):
            print(name[key])


if __name__ == "__main__":
    main()
