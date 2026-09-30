def validate_password(password: str) -> tuple[bool, list[str]]:
    """Validates a password using standard loops and string methods."""
    # Track which character types we find in the password
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False

    # Define our special character set
    special_characters = '!@#$%^&*()_+-=[]{}|;:",.<>?/'

    # Check length first
    is_long_enough = len(password) >= 10

    # Loop through each character in the password
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

    # Build the list of missing requirements
    errors = []
    if not is_long_enough:
        errors.append("At least 10 characters long")
    if not has_uppercase:
        errors.append("At least one uppercase letter (A-Z)")
    if not has_lowercase:
        errors.append("At least one lowercase letter (a-z)")
    if not has_digit:
        errors.append("At least one number (0-9)")
    if not has_special:
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