"""The menu should have four separate options:

(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit"""

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

LINE = "*" * 30
result = "No result received."
score = 0


def main():
    """Gets user score and describes result. """
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

                result = categorize_result(score)
                print(f"Score received.")

        elif choice == "2":
            print(result)

        elif choice == "3":
            star_score = "*" * len(math.floor(score))
            print(f"Star score: {star_score}")
            break

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter G, 1, 2 or 3.")


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


# Program entry point
main()
