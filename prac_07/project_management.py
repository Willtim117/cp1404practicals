"""
Project Management
Estimate: 3 hr
Actual:
"""
from prac_07.project import Project

"""
Name	Start Date	Priority	Cost Estimate	Completion Percentage
Build Car Park	12/09/2021	2	600000.0	95
Mow Lawn	31/10/2022	3	3.0	0
Organise Pantry	20/07/2022	1	25.0	55
Record Music Video	01/12/2022	9	250000.0	0
Read 7 Habits Book	13/12/2021	6	99.0	100
"""

FILENAME = "projects.txt"


def main():
    """Read file of programming language details, save as objects, display."""

    projects = load_file(FILENAME)

    for project in projects:
        print(project)


def load_file(filename):
    """Load guitar data from a CSV file into a list of Guitar objects."""
    projects = []
    # Open the file for reading
    in_file = open(filename, 'r')

    in_file.readline()

    for line in in_file:
        # e.g. Martin Grand J12-16GTE,2015,2199
        parts = line.strip().split('\t')
        project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), float(parts[4]))
        print(parts)

        projects.append(project)
    in_file.close()
    return projects


main()
