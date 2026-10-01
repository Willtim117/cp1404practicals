"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    - When input is not integer
2. When will a ZeroDivisionError occur?
    - Valid numerator input and denominator input is 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    - while loop until input makes denominator integer not 0
"""
try:
    numerator = int(input("Enter the numerator: "))
    # avoid ZeroDivisionError
    denominator = 0
    while denominator == 0:
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
