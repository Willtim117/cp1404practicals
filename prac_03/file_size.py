"""Write a program that asks the user for a filename, then prints the number of lines in that file."""


def main():
    """Ask for name. Print number of lines in file."""
    print("Please enter a valid file name")
    print(f"Q - Quit")

    file_name = input("Enter Filename: ").strip()

    while file_name != "Q":
        try:
            file_size = number_of_lines(file_name)
            print(f"{file_name} has {file_size} lines.")
        except FileNotFoundError:
            print(f"ERROR: {file_name} does not exist.")
        except OSError:
            print("Invalid Input")
        file_name = input("Enter Filename: ").strip()


def number_of_lines(file_name):
    """count total number of lines inside file"""
    with open(file_name, "r") as open_file:
        total_lines = 0
        for i, line in enumerate(open_file):
            # Summing all the lines
            total_lines += 1
    return total_lines


main()
