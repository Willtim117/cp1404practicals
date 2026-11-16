"""
Project Management
Estimate: 3 hr
Actual:
"""
import csv
from datetime import datetime
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
test_file = "test_file.txt"


def main():
    """Read file of programming language details, save as objects, display."""

    menu = """
    Main Menu
    ---------
    - (L)oad projects  
    - (S)ave projects  
    - (D)isplay projects  
    - (F)ilter projects by date
    - (A)dd new project  
    - (U)pdate project
    - (Q)uit
    """
    print(menu)

    projects = []
    choice = input(">>> ").strip().upper()
    while choice != "Q":
        if choice == "L":
            # projects = load_file(FILENAME)
            projects = load_file(test_file)
            print("INCOMPLETE CODE")

        elif choice == "S":
            print("INCOMPLETE CODE")

        elif choice == "D":
            display_projects(projects)
            print("INCOMPLETE CODE")

        elif choice == "F":
            print("INCOMPLETE CODE")

        elif choice == "A":
            add_project(projects)
            print("INCOMPLETE CODE")

        elif choice == "U":
            update_file(projects, test_file)
            print("INCOMPLETE CODE")

        else:
            print("INVALID INPUT")

        print(menu)
        choice = input(">>> ").strip().upper()

        "<do final thing, if needed>"


def load_file(filename) -> list[Project]:
    """
    Load guitar data from a CSV file into a list of Guitar objects.
    Name	Start Date	Priority	Cost Estimate	Completion Percentage
    Build Car Park	12/09/2021	2	600000.0	95
    """
    projects = []
    # Open the file for reading
    in_file = open(filename, 'r')

    next(in_file)

    for line in in_file:
        # e.g. Martin Grand J12-16GTE,2015,2199
        parts = line.strip().split('\t')
        project = Project(parts[0], parse_date(parts[1]), int(parts[2]),
                          float(parts[3]), float(parts[4]))
        print(parts)

        projects.append(project)
    in_file.close()
    return projects


def update_file(projects: list[Project], filename: str):
    """Write/Overwrite the list of projects into the given text file."""
    with open(filename, "w", newline='') as out_file:
        writer = csv.writer(out_file, delimiter='\t')

        writer.writerow(["Name", "Start Date", "Priority", "Cost Estimate", "Completion Percentage"])

        for project in projects:
            writer.writerow([project.name, project.start_date.strftime("%d/%m/%Y"),
                             project.priority, project.cost_estimate, project.completion_percentage])


def add_project(projects: list[Project]):
    """
    Name	Start Date	Priority	Cost Estimate	Completion Percentage
    Build Car Park	12/09/2021	2	600000.0	95
    """
    print("Let's add a new project")

    name = str(input("Name: "))
    while name != "":
        date_string = input("Start date (dd/mm/yy): ")
        start_date = parse_date(date_string)

        priority = int(input("Priority: "))
        cost_estimate = float(input("Cost estimate: "))
        percentage = float(input("Percentage complete: "))

        projects.append(Project(name, start_date, priority, cost_estimate, percentage))

        print(f"{name} added. {start_date}. Priority: {priority}. Estimate: ${cost_estimate}. "
              f"Percentage Complete: {percentage}% ")

        name = str(input("Name: "))


def display_projects(projects: list[Project]):
    """Takes list of Guitar objects print formatted list."""

    name_width = max(len(f"{project.name}") for project in projects)
    cost_width = max(len(f"{project.cost_estimate:,.2f}") for project in projects)

    incomplete_projects = []
    complete_projects = []

    """format_date = will_date.strftime("%d of %B (which is a %A)")"""
    for i, project in enumerate(projects):
        if project.completion_percentage == 100.0:
            complete_projects.append(project)
        else:
            incomplete_projects.append(project)

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"\t{project.name:<{name_width}}: start: {project.start_date.strftime("%d/%m/%Y")}, "
              f"priority:{project.priority:>{2}}, Estimate: ${project.cost_estimate:>{cost_width}}, "
              f"Completion: {project.completion_percentage:>{4}}%")

    print("Completed projects:")
    for project in complete_projects:
        print(f"\t{project.name:<{name_width}}: start: {project.start_date.strftime("%d/%m/%Y")}, "
              f"priority:{project.priority:>{2}}, Estimate: ${project.cost_estimate:>{cost_width}}, "
              f"Completion: {project.completion_percentage:>{4}}%")


def parse_date(date_string: str):
    """Parse a date in either dd/mm/yyyy or dd/mm/yy format."""
    for fmt in ("%d/%m/%Y", "%d/%m/%y"):
        try:
            return datetime.strptime(date_string, fmt).date()
        except ValueError:
            continue
    raise ValueError(f"Invalid date: {date_string}")


main()
