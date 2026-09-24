"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""


MENU = """Enter Sales value
Enter Q to Quit"""
print(MENU)
while True:
    sales_input = input("Enter sales: $").strip().upper()
    if sales_input == "Q":
        break
    try:
        user_sales = float(sales_input)
    except ValueError:
        print("Enter sales again")
        continue
    if 0 <= user_sales < 1000:
        user_bonus = 0.1*user_sales
    elif user_sales >= 1000:
        user_bonus = 0.15*user_sales
    else:
        print("Enter sales again")
        continue
    print(f"Bonus is: ${user_bonus:.2f}")
print("Thank you.")

