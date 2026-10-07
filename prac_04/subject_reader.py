"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Program to load and display subject data from file."""
    data_list = load_data(FILENAME)
    print(data_list)


def load_data(filename=FILENAME) -> list[list]:
    """Return a data list from a formatted file.txt with each line: subject,lecturer,number of students."""
    data_list = []
    input_file = open(filename)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        # Make the number an integer as part of a new, poorly named, list
        data = [parts[0], parts[1], int(parts[2])]
        print(data)  # See if that worked
        print("----------")
        data_list.append(data)
        # print(data_list)
    input_file.close()
    return data_list


main()
