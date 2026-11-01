"""
Emails
Estimate: 45 minutes
Actual:   40 minutes
"""


def main():
    """Stores users' emails (unique keys) and names (values) in a dictionary.
    Then prints dictionary"""

    email_to_name = {}
    get_email = input("Enter Email: ")

    while get_email != "":

        suggested_name = extract_name(get_email)
        # Validate Name
        is_name_valid = input(f"Is your name {suggested_name}? (Y/N)").strip().lower()
        if is_name_valid == "" or is_name_valid == "y":
            name = suggested_name
        else:
            name = input("Name: ").strip().title()
        # Build Dictionary
        email_to_name[get_email] = name
        get_email = input("Enter Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract a possible name from an Email Address."""
    email_name = email.split("@")[0]
    suggested_name = email_name.replace('.', ' ').title()
    return suggested_name


main()
