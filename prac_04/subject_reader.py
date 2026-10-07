"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Program to load and display subject data from file."""
    data_list, max_name_length, max_num_students_length = load_data(FILENAME)
    for line in data_list:
        print(f"{line[0]} is taught by {line[1]:{max_name_length}} "
              f"and has {line[2]:>{max_num_students_length}} students")


def load_data(filename=FILENAME) -> tuple[list[list], int, int]:
    """Return a data list and category lengths from a formatted file.txt
    with each line: subject,lecturer,number of students."""
    # initial variables
    data_list = []
    max_name_length = 0
    max_num_students_length = 0

    input_file = open(filename)

    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts

        # Make the number an integer as part of a new, poorly named, list
        data = [parts[0], parts[1], int(parts[2])]

        # Get longest character width of lecturer name
        if max_name_length < len(parts[1]):
            max_name_length = len(parts[1])
        # Get longest character width of student numbers
        if max_num_students_length < len(parts[2]):
            max_num_students_length = len(parts[2])

        data_list.append(data)
        # print(data_list)
    input_file.close()
    return data_list, max_name_length, max_num_students_length


main()
