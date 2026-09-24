"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""

MENU = """CF - Convert Celsius to Fahrenheit
FC - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "CF":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "FC":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = (5/9.0)*(fahrenheit - 32)
        print(f"Result: {celsius:.2f} C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
