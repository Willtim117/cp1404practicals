"""Complete BMI program"""


def main():
    height = float(input("Height (m): "))
    weight = float(input("Weight (kg): "))
    bmi = calculate_bmi(height, weight)
    print(f"Your BMI is {bmi:.2f}.")


def calculate_bmi(height, weight):
    return weight / (height ** 2)


main()
