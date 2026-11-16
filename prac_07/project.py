"""
Project
Estimate: 3 hr
Actual:
"""
import datetime


class Project:
    """Represent a Project."""

    def __init__(self, name="", start_date=None, priority="", cost_estimate="", completion_percentage=""):
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

    # def get_age(self):
    #     age = datetime.datetime.now().year - self.year
    #     return age
    #
    # def is_vintage(self):
    #     return self.get_age() >= 50
    #
    # def __lt__(self, other):
    #     """Determine if two People are the same."""
    #     if not isinstance(other, Guitar):
    #         return NotImplemented
    #     return self.year < other.year

