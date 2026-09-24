"""
CP1404/CP5632 - Practical
Program to determine score status
"""

while True:
    user_input = input("Enter score (or Q to quit): ").strip()

    if user_input.upper() == "Q":
        print("Thank you")
        break

    try:
        score = float(user_input)
    except ValueError:
        print("Invalid Input")
        continue

    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    elif score >= 0:
        print("Bad")
    else:
        print("Invalid Input")


def main():
    while True:
        user_input = input("Enter score (or Q to quit): ").strip()

        if user_input.upper() == "Q":
            print("Thank you")
            break

        try:
            score = float(user_input)
        except ValueError:
            print("Invalid Input")
            continue

        else:
            result = categorize_result(user_input)
            print(result)




def categorize_result(score: float) -> str:
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    elif score >= 0:
        result = "Bad"
    else:
        result = "Invalid Input"
    return result

