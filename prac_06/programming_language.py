"""
Programming Language
Estimate: 1 hr
Actual:
"""


class ProgrammingLanguage:
    """Represent a Programming Language."""

    def __init__(self, name="", typing="", reflection=False, year=0):
        """Initialize a ProgramLanguage instance.

        """
        self.name = name
        self.typing = typing.upper()
        self.reflection = reflection
        self.year = year

    def __str__(self) -> str:
        """Return string representation of a ProgrammingLanguage"""
        return f"{self.name}, Typing:{self.typing.title()}, Reflection={self.reflection}, First appeared in {self.year}"

    def __repr__(self) -> str:
        return str(self)

    def is_dynamic(self) -> bool:
        """Return True if the Programming Language is Dynamically typed."""
        return self.typing == "DYNAMIC"
