"""
Ohjelmointi 1 / Programming 1
Paracetamol/Panadol/Tylenol Dosing Advisor
"""

def calculate_dose(w, t, td, a):
    doseToGive = w*15 
    minTIme = 6



def main():
    weight = int(input("Patient's weight (kg): "))
    time = int(input("How much time has passed from the previous dose (full hours): "))
    total_dose = int(input("The total dose for the last 24 hours (mg): "))
    amount = int(input("The amount of Parasetamol to give to the patient: "))

    # calculate_dose assumes parameters to be of type int
    # and they should be passed in the order: weight, time, total_doze_24
    # (or more like the automated tests assume this)

    calculate_dose(weight, time, total_dose, amount)

if __name__ == "__main__":
  main()