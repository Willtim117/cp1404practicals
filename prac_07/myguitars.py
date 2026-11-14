"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
(contains multiple versions for demonstration: using csv and namedtuple)
"""

import csv
from symtable import Class

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read file of programming language details, save as objects, display."""
    guitars = []
    # Open the file for reading
    in_file = open(FILENAME, 'r')

    for line in in_file:
        parts = line.strip().split(',')
        # Martin Grand J12-16GTE,2015,2199
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        # Add the language we've just constructed to the list
        guitars.append(guitar)
    # Close the file as soon as we've finished reading it
    in_file.close()

    # Loop through and display all guitars (using their str method)
    guitars.sort()
    for guitar in guitars:
        print(guitar)

    print("My Guitars!")
    name = str(input("Name: "))
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))

        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year} : ${cost:,.2f}) added.")

        name = str(input("Name: "))

    name_width = max(len(f"{guitar.name}") for guitar in guitars)
    price_width = max(len(f"{guitar.cost:,.2f}") for guitar in guitars)

    print("These are my Guitars:")
    for i, guitar in enumerate(guitars):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i + 1}: {guitar.name:>{name_width}} ({guitar.year}), worth $ {guitar.cost:>{price_width},.2f} "
              f"{vintage_string}")

    update_file(guitars, FILENAME)


def update_file(guitars: list[Guitar], filename: str):
    """Overwrite Guitars list into the given CSV file"""
    with open(filename, "w", newline='') as out_file:
        writer = csv.writer(out_file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


main()
