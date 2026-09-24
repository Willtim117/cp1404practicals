"""Electricity bill estimator
Enter cents per kWh: 35
Enter daily use in kWh: 4.5
Enter number of billing days: 90
Estimated bill: $141.75 """

program_name = ("Electricity bill Estimator")
print(program_name)

# Tariff ($ per kWh)
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

while True:

    which_tariff = int(input("Which tariff? 11 or 31: "))
    if which_tariff == 11:
        tariff_selected = TARIFF_11
    elif which_tariff == 31:
        tariff_selected = TARIFF_31

    daily_kWh = float(input("Enter daily use in kWh: "))
    num_bill_days = int(input("Enter number of billing days: "))

    estimated_bill = (tariff_selected*daily_kWh*num_bill_days)
    print(f"Estimated Bill: ${estimated_bill:.2f}")

    while True:
        continue_program = input("Continue? ").strip().upper()
        if continue_program in ("Y", "N"):
         break
        print("Invalid Message")

    if continue_program == "N":
        break

print("Thank you")
