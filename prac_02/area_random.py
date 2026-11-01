"""Import modules to use 'extra' features in Python"""

import random

length = int(input("Length: "))
width = random.randint(1, length)
area = length * width

print(f"Area of {length} x {width} is {area}.")


def print_grid(number_rows, number_columns):
    for i in range(number_rows):
        print("*" * number_columns)


print_grid(4, 6)
