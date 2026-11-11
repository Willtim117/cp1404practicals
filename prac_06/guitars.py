"""
Guitars
Estimate: 1 hr
Actual: 45 mins
"""
# class Student:
#     def __init__(self, first_name="", last_name="", student_id=0):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.id = student_id
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name} ({self.id})"
#
#
# # Simple example class usage (client code)
# first_name = input("First name: ")
# last_name = input("Last name: ")
# student_id = int(input("ID: "))
# s1 = Student(first_name, last_name, student_id)
# print(s1.first_name, "has ID", s1.id)


my_guitars = [["Fender Stratocaster", 2014, 765.4], ["Gibson L-5 CES", 1922, 16035.40],
              ["Line 6 JTV-59", 2010, 1512.90]]

print("My Guitars!")
name = str(input("Name: "))
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: "))

    my_guitar = [name, year, cost]
    my_guitars.append(my_guitar)
    print(f"{name} ({year} : ${cost:,.2f}) added.")

    name = str(input("Name: "))

print("These are my Guitars:")
name_width = max(len(f"{guitar[0]}") for guitar in my_guitars)
price_width = max(len(f"{guitar[2]:,.2f}") for guitar in my_guitars)

for i, guitar in enumerate(my_guitars):
    print(f"Guitar {i+1}: {guitar[0]:>{name_width}} ({guitar[1]}), worth $ {guitar[2]:>{price_width},.2f}")
    # TODO "Vintage"

