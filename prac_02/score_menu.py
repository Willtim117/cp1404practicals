"""The menu should have four separate options:

Get a valid score (must be 0-100 inclusive)
Print result (copy or import your function to determine the result from score.py)
Show stars (this should print as many stars as the score)
Quit"""

import math

# Constants
MENU = """
Main Menu
---------
1. Get a valid score (0-100 inclusive)
2. Print result
3. Show stars
0. Quit
Enter choice: """


def main():
    """Gets user score and describes result. """
    score = 0
    result = "result not received."

    while True:
        choice = input(MENU).strip()

        if choice == "1":

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

                result, is_score_valid = categorize_result(score)

                if not is_score_valid:
                    print("Invalid Score. Score is 0 - 100.")
                else:
                    print(f"Score received.")

                break

        elif choice == "2":
            print(f"Score {score:.1f} is {result}.")

        elif choice == "3":
            star_score = "*" * math.floor(score)
            print(f"Star score: {star_score}")

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 0, 1, 2 or 3.")


def categorize_result(score: float) -> tuple[str, bool]:
    """Take score, categorize result and return result"""
    is_score_valid = True
    if score < 0 or score > 100:
        result = "Invalid score"
        is_score_valid = False
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    elif score >= 0:
        result = "Bad"
    else:
        result = "Invalid Input"
        is_score_valid = False
    return result, is_score_valid


# Program entry point
main()
