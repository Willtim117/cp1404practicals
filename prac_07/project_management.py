"""
Project Management
Estimate: 3 hr
Actual:
"""
import csv
from datetime import datetime
from prac_07.project import Project

# FILENAME = "projects.txt"
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
    print("Welcome to Pythonic Project Management\nPlease load a project.")
    print(menu)

    projects = []
    choice = input(">>> ").strip().upper()
    while choice != "Q":

        if choice == "L":
            """Load Projects"""
            FILENAME = get_filename()
            projects = load_file(FILENAME)

        elif choice == "S":
            """Save Projects"""
            save_file(projects)

        elif choice == "D":
            """Display Projects"""
            display_projects(projects)

        elif choice == "F":
            """Filter projects by date"""
            filter_by_date(projects)

        elif choice == "A":
            """Add new project"""
            add_project(projects)

        elif choice == "U":
            """Update project"""
            update_project(projects)

        else:
            print("INVALID INPUT")

        print(menu)
        choice = input(">>> ").strip().upper()

    save_choice = str(input("Would you like to save projects? Y/N ")).upper()
    while save_choice != "N":
        if save_choice == "Y":
            save_file(projects)
            break
        print("Invalid input. Y/N")
        save_choice = str(input("Would you like to save projects? Y/N ")).upper()

    print("Thank you for using custom-built project management software.")


def get_filename():
    """Gets name from user creates name.txt"""
    filename = input("Name of text file to load: ").strip()
    if not filename.lower().endswith(".txt"):
        filename += ".txt"
    return filename


def load_file(filename) -> list[Project]:
    """Load projects from a text file. Return empty list if file doesn't exist."""
    projects = []
    try:
        with open(filename, "r") as in_file:
            next(in_file)
            for line in in_file:
                # Name	Start Date	Priority	Cost Estimate	Completion Percentage
                parts = line.strip().split('\t')
                project = Project(parts[0], parse_date(parts[1]), int(parts[2]),
                                  float(parts[3]), float(parts[4]))

                projects.append(project)

        print(f"Loaded {len(projects)} projects from {filename}")

    except FileNotFoundError:
        print(f"File '{filename}' not found. Starting with empty project list.")

    return projects


def save_file(projects: list[Project]):
    """Write/Overwrite the list of projects into the given text file."""
    filename = str(input("Name of file to save projects to: "))
    if not filename.lower().endswith(".txt"):
        filename += ".txt"
    with open(filename, "w", newline='') as out_file:
        writer = csv.writer(out_file, delimiter='\t')

        writer.writerow(["Name", "Start Date", "Priority", "Cost Estimate", "Completion Percentage"])

        for project in projects:
            writer.writerow([project.name, project.start_date.strftime("%d/%m/%Y"),
                             project.priority, project.cost_estimate, project.completion_percentage])
    print(f"{filename} saved.")


def display_projects(projects: list[Project]):
    """Takes list of Project objects prints formatted list."""

    name_width, cost_width = find_widths(projects)
    if name_width == 0:
        return

    incomplete_projects = []
    complete_projects = []

    """format_date = will_date.strftime("%d of %B (which is a %A)")"""
    for i, project in enumerate(projects):
        if project.is_complete():
            complete_projects.append(project)
        else:
            incomplete_projects.append(project)

    incomplete_projects.sort()
    complete_projects.sort()

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"\t{project.name:<{name_width}}: start: {project.start_date.strftime("%d/%m/%Y")}, "
              f"priority:{project.priority:>{2}}, Estimate: $ {project.cost_estimate:>{cost_width},.2f}, "
              f"Completion: {project.completion_percentage:>{4}}%")

    print("Completed projects:")
    for project in complete_projects:
        print(f"\t{project.name:<{name_width}}: start: {project.start_date.strftime("%d/%m/%Y")}, "
              f"priority:{project.priority:>{2}}, Estimate: $ {project.cost_estimate:>{cost_width},.2f}, "
              f"Completion: {project.completion_percentage:>{4}}%")


def filter_by_date(projects: list[Project]):
    """Gets date then displays formatted list of projects started after date."""
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    start_date = parse_date(date_string)

    valid_projects = [project for project in projects if project.start_date > start_date]

    if not valid_projects:
        print(f"No projects found after {start_date}.")
        return

    name_width, cost_width = find_widths(projects)
    print("Projects:")
    for project in valid_projects:
        print(f"\t{project.name:<{name_width}}: start: {project.start_date.strftime("%d/%m/%Y")}, "
              f"priority:{project.priority:>{2}}, Estimate: $ {project.cost_estimate:>{cost_width},.2f}, "
              f"Completion: {project.completion_percentage:>{5}}%")


def add_project(projects: list[Project]):
    """ Gets user input: Name, Start Date, Priority, Cost Estimate, Completion Percentage.
    Creates new Project object. Appends Object to project list.
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

        print(f"{name} added. {start_date}. Priority: {priority}. Estimate: $ {cost_estimate:,.2f}. "
              f"Percentage Complete: {percentage}% ")

        name = str(input("Name: "))


def parse_date(date_string: str):
    """Parse a date in either dd/mm/yyyy or dd/mm/yy format."""
    for fmt in ("%d/%m/%Y", "%d/%m/%y"):
        try:
            return datetime.strptime(date_string, fmt).date()
        except ValueError:
            continue
    raise ValueError(f"Invalid date: {date_string}")


def update_project(projects: list[Project]):
    """Gets user project selection. Allows user to update percentage and priority of selected Project object."""

    name_width, cost_width = find_widths(projects)
    if name_width == 0:
        return

    projects.sort()

    print("Projects:")
    for i, project in enumerate(projects):
        print(f"\t{i:3}. {project.name:<{name_width}}: start: {project.start_date.strftime("%d/%m/%Y")}, "
              f"priority:{project.priority:>{2}}, Estimate: $ {project.cost_estimate:>{cost_width},.2f}, "
              f"Completion: {project.completion_percentage:>{5}}%")

    project_index = int(input("Project choice: "))
    print(f"\t{project_index:3}. {projects[project_index].name:<{name_width}}: "
          f"start: {projects[project_index].start_date.strftime("%d/%m/%Y")}, "
          f"priority:{projects[project_index].priority:>{2}}, "
          f"Estimate: $ {projects[project_index].cost_estimate:>{cost_width},.2f}, "
          f"Completion: {projects[project_index].completion_percentage:>{5}}%")

    new_percentage = input("New Percentage: ").strip()
    if new_percentage:
        projects[project_index].completion_percentage = float(new_percentage)

    new_priority = input("New Priority: ").strip()
    if new_priority:
        projects[project_index].priority = int(new_priority)

    print(f"{projects[project_index].name} has been updated.")


def find_widths(projects: list[Project]):
    """Finds maximums widths of Project name and Project Cost. To help with display formats."""
    try:
        name_width = max(len(f"{project.name}") for project in projects)
        cost_width = max(len(f"{project.cost_estimate:,.2f}") for project in projects)
        return name_width, cost_width
    except ValueError:
        print("No Projects to display. Get your grind on.")
        return 0, 0


main()
