"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random


def main():
    """Gets user score and describes result. """
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

        result = categorize_result(score)
        print(f"User score {user_input} is {result}")

        # Excellent result prize feature
        if result == "Excellent":
            print("You get a prize!")

        # Random score and result feature
        random_score = random.uniform(0, 100)
        random_result = categorize_result(random_score)
        print(f"Random: {random_score:.1f} = {random_result}")


def categorize_result(score: float) -> str:
    """Take score, categorize result and return result"""
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


main()
