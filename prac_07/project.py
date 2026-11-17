"""
Project
Estimate: 3 hr
Actual: 5 hr
"""


class Project:
    """Represent a Project."""

    def __init__(self, name="", start_date=None, priority="", cost_estimate="", completion_percentage=0.0):
        """Initialize a Project instance.
        """
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self) -> str:
        """Return string representation of a Guitar"""
        return (f"{self.name}, {self.start_date.strftime("%d/%m/%Y")},"
                f" {self.priority}, {self.cost_estimate}, {self.completion_percentage}")

    def __repr__(self) -> str:
        return str(self)

    def __lt__(self, other):
        return self.priority < other.priority

    def is_complete(self):
        return self.completion_percentage >= 100
