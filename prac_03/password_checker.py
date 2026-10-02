"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 7
MAX_LENGTH = 15
IS_SPECIAL_CHARACTER_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters (A-Z)")
    print("\t1 or more lowercase characters (a-z)")
    print("\t1 or more numbers (0-9)")

    if IS_SPECIAL_CHARACTER_REQUIRED:
        print("\t1 or more special characters: ", SPECIAL_CHARACTERS)

    password = input("Enter your new password: ")
    is_valid, errors = is_valid_password(password)

    while not is_valid:
        print("Invalid password!")
        for error in errors:
            print(f"    Missing: {error}")
        password = input("Enter your new password: ")
        is_valid, errors = is_valid_password(password)

    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password: str) -> tuple[bool, list[str]]:
    """Determine if the provided password is valid."""
    # if length is wrong, return False
    is_length_valid = MIN_LENGTH <= len(password) <= MAX_LENGTH

    number_of_lower = 0
    number_of_upper = 0
    number_of_digit = 0
    number_of_special = 0

    # Count each kind of character (use str methods like isdigit)
    for character in password:
        if character.islower():
            number_of_lower += 1
        elif character.isupper():
            number_of_upper += 1
        elif character.isdigit():
            number_of_digit += 1
        elif character in SPECIAL_CHARACTERS:
            number_of_special += 1

        pass

    # Build the list of missing requirements
    errors = []
    if number_of_lower == 0:
        errors.append("At least one lowercase letter (a-z)")
    if number_of_upper == 0:
        errors.append("At least one uppercase letter (A-Z)")
    if number_of_digit == 0:
        errors.append("At least one number (0-9)")
        # If special characters are required, then check the count of those
        # and return False if it's zero
    if IS_SPECIAL_CHARACTER_REQUIRED:
        if number_of_special == 0:
            errors.append("At least one special character (!@#$%^&* etc.)")
    if not is_length_valid:
        errors.append(f"Must be between {MIN_LENGTH} and {MAX_LENGTH} characters long")

    # if we get here (without returning False), then the password must be valid
    is_valid = len(errors) == 0
    return is_valid, errors


if __name__ == "__main__":
    main()
