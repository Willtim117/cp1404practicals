"""
Guitars
Estimate: 1 hr
Actual: 1 hr 30 mins
"""

from guitar import Guitar
from prac_06.guitar import Guitar

my_guitars = []

my_guitars.append(Guitar("Fender Stratocaster", 2014, 765.4))
my_guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
my_guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))


print("My Guitars!")
name = str(input("Name: "))
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: "))

    my_guitars.append(Guitar(name, year, cost))
    print(f"{name} ({year} : ${cost:,.2f}) added.")

    name = str(input("Name: "))

name_width = max(len(f"{guitar.name}") for guitar in my_guitars)
price_width = max(len(f"{guitar.cost:,.2f}") for guitar in my_guitars)

print("These are my Guitars:")
for i, guitar in enumerate(my_guitars):
    vintage_string = "(vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i+1}: {guitar.name:>{name_width}} ({guitar.year}), worth $ {guitar.cost:>{price_width},.2f} "
          f"{vintage_string}")
