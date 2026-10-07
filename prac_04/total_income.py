"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    for line in build_report(incomes, number_of_months):
        print(line)


def build_report(incomes: list, number_of_months: int) -> list:
    """Build and return lines of income report."""
    total = 0
    income_report = ["\nIncome Report\n-------------"]
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        total += income
        income_report.append(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")
    return income_report


main()
