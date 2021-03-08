def read_file(fileName):
    with open(fileName, "r") as f:
        file = f.readlines()

        contacts = {}

        first_line = True
        tmp = []
        for row in file:
            rows = row.split(";")

            if first_line:
                tmp = rows

                first_line = False
                continue

            temp = {}
            for ihansama in range(1, len(rows)):
                temp[tmp[ihansama].strip()] = rows[ihansama].strip()

            contacts[rows[0]] = temp

        return contacts
