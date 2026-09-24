"""Number of items: 3
Price of item: 100
Price of item: 35.56
Price of item: 3.24
Total price for 3 items is $124.92 """

gross_price = 0

# ------- Validate number of items ------
while True:
    try:
        number_of_items = int(input("Enter Number of Items: ").strip().upper())
        if number_of_items < 0:
            print("Number of items cannot be negative.")
            continue
        break
    except ValueError:
        print("Please enter whole number.")

# ------ Enter Item Prices and Add Gross and Net Price ------
item_count = number_of_items
while item_count != 0:
    price_of_item = float(input("Price of item: "))
    item_count = item_count - 1
    gross_price = gross_price + price_of_item
    continue
if gross_price >= 100:
    net_price = gross_price * 0.9
else:
    net_price = gross_price

# ----- Print Receipt -------
print(f"Thank you.\n"
      f"Number of items: {number_of_items}\n"
      f"Gross Price is ${gross_price:.2f}\n"
      f"Net price is ${net_price:.2f}")
