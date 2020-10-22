days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for month in range(12):
    for y in range(days[month]):
        print(f"{day + 7}.{month + 1}.")
