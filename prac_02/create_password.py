import re


def validate_password(password: str) -> tuple[bool, list[str]]:
    """Validates a password against traditional complexity rules."""
    errors = []

    if len(password) < 10:
        errors.append("At least 10 characters long")
    if not re.search(r"[A-Z]", password):
        errors.append("At least one uppercase letter (A-Z)")
    if not re.search(r"[a-z]", password):
        errors.append("At least one lowercase letter (a-z)")
    if not re.search(r"[0-9]", password):
        errors.append("At least one number (0-9)")
    if not re.search(r'[!@#$%^&*()_+\-=\[\]{}|;:",.<>?/]', password):
        errors.append("At least one special character (!@#$%^&* etc.)")

    is_valid = len(errors) == 0
    return is_valid, errors


def main():
    print("=== Create a New Password ===")
    print("Requirements:")
    print(" - Minimum 10 characters")
    print(" - At least 1 uppercase letter")
    print(" - At least 1 lowercase letter")
    print(" - At least 1 digit")
    print(" - At least 1 special character\n")

    while True:
        password = input("Enter your new password: ")
        is_valid, errors = validate_password(password)

        if is_valid:
            print("\nPassword successfully created!")
            # Displays matching number of asterisks corresponding to length
            masked_password = "*" * len(password)
            print(f"Stored Password: {masked_password}")
            break
        else:
            print("\nPassword does not meet requirements:")
            for error in errors:
                print(f"  - Missing: {error}")
            print("\nPlease try again.\n")


if __name__ == "__main__":
    main()

