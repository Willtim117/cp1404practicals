"""
Name Menu Program
A simple menu-driven program that:
- Gets a valid (non-empty) name from the user
- Prints a greeting surrounded by decorative lines
- Prints a randomly varied "secret" version of the name
"""

import random

# Constants
MENU = """
Main Menu
---------
1. Get valid name
2. Print greeting with lines
3. Print secret name (random variation)
0. Quit
Enter choice: """

LINE = "*" * 30


def get_valid_name():
    """Prompt the user until a non-empty name is entered and return it."""
    while True:
        name = input("Enter your name: ").strip()
        if name:  # non-empty after stripping whitespace
            return name
        print("Name cannot be empty. Please try again.")


def print_greeting(name):
    """Print a greeting for the given name, framed by decorative lines."""
    print(LINE)
    print(f"Hello, {name}!")
    print(LINE)


def print_secret_name(name):
    """Create and print a random variation of the name (letter shuffle)."""
    letters = list(name)
    random.shuffle(letters)
    secret = "".join(letters)
    print(f"Your secret name is: {secret}")


def main():
    """Display the main menu and handle user choices."""
    name = None  # will hold the validated name once obtained

    while True:
        choice = input(MENU).strip()

        if choice == "1":
            name = get_valid_name()
            print(f"Name set to: {name}")

        elif choice == "2":
            if name is None:
                print("Please get a valid name first (option 1).")
            else:
                print_greeting(name)

        elif choice == "3":
            if name is None:
                print("Please get a valid name first (option 1).")
            else:
                print_secret_name(name)

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 0, 1, 2 or 3.")


# Program entry point
main()
