"""
Guitar
Estimate: 1 hr
Actual:
"""
import datetime


class Guitar:
    """Represent a Guitar."""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialize a Guitar instance.
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self) -> str:
        """Return string representation of a Guitar"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __repr__(self) -> str:
        return str(self)

    def get_age(self):
        age = datetime.datetime.now().year - self.year
        return age

    def is_vintage(self):
        return self.get_age() >= 50
