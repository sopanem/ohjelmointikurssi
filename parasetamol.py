
def calculate_dose(weight, previous, total):
    if previous < 6:
        return 0

    return min(weight * 15, 4000 - total)


def main():
    weight = int(input("Patient's weight (kg): "))
    previous = int(
        input("How much time has passed from the previous dose (full hours): "))
    total = int(input("The total dose for the last 24 hours (mg): "))
    print(
        f"The amount of Parasetamol to give to the patient: {calculate_dose(weight, previous, total)}")


if __name__ == "__main__":
    main()
