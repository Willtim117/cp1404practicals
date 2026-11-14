"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
(contains multiple versions for demonstration: using csv and namedtuple)
"""

import csv
from collections import namedtuple

from guitar import Guitar

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


main()
