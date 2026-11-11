"""
Guitar
Estimate: 1 hr
Actual: 45 mins
"""

from guitar import Guitar
from prac_06 import guitar

# Create guitars
gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
another = Guitar("Another Guitar", 2013, 1512.9)

# Test get_age()
print(f"{gibson.name} get_age() - Expected {2026 - 1922}. Got {gibson.get_age()}")
print(f"{another.name} get_age() - Expected {2026 - 2013}. Got {another.get_age()}")

# Test is_vintage()
print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
print(f"{another.name} is_vintage() - Expected False. Got {another.is_vintage()}")

# String
print(gibson)
print(another)
