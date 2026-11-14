"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
(contains multiple versions for demonstration: using csv and namedtuple)
"""

import csv
from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read file of programming language details, save as objects, display."""

    guitars = load_file(FILENAME)
    print_list(guitars)

    add_guitar(guitars)

    guitars.sort()

    print_list(guitars)

    update_file(guitars, FILENAME)


def load_file(filename):
    """Load guitar data from a CSV file into a list of Guitar objects."""
    guitars = []
    # Open the file for reading
    in_file = open(filename, 'r')

    for line in in_file:
        # e.g. Martin Grand J12-16GTE,2015,2199
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))

        guitars.append(guitar)
    in_file.close()
    return guitars


def update_file(guitars: list[Guitar], filename: str):
    """Overwrite Guitars list into the given CSV file"""
    with open(filename, "w", newline='') as out_file:
        writer = csv.writer(out_file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


def add_guitar(guitars: list[Guitar]):

    print("Add Guitars")
    name = str(input("Name: "))
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))

        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year} : ${cost:,.2f}) added.")

        name = str(input("Name: "))


def print_list(guitars: list[Guitar]):
    """Takes list of Guitar objects print formatted list."""

    index_width = len(str(len(guitars)))
    name_width = max(len(f"{guitar.name}") for guitar in guitars)
    year_width = max(len(f"{guitar.year}") for guitar in guitars)
    price_width = max(len(f"{guitar.cost:,.2f}") for guitar in guitars)

    print("Guitar List:")
    for i, guitar in enumerate(guitars):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i + 1:>{index_width}}: {guitar.name:>{name_width}} ({guitar.year:>{year_width}}), "
              f"worth $ {guitar.cost:>{price_width},.2f} {vintage_string}")


main()
