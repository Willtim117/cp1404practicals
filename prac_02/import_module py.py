"""Import modules to use 'extra' features in Python"""

import random

low = int(input("Low: "))
high = int(input("High: "))

secret = random.randint(low, high)
guess = int(input("Guess: "))

while guess != secret:
    print("Incorrect")
    guess = int(input("Guess: "))
print("Got it!")

length = int(input("Length: "))
width = random.randint(1, length)
area = length*width
print(f"Area of {length} x {width} is {area}.")