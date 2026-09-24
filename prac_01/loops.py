"""the following for loop that displays all the odd numbers between"""
"one and twenty with a space between each one."

for i in range(1, 21, 2):
    print(i, end=' ')
print()

"a. count in 10s from 0 to 100"
for i in range(0,101,10):
    print(i, end=' ')
print()

"b. count down from 20 to 1"
for i in range(20,0,-1):
    print(i, end=' ')
print()

"c. print a number of stars."
number_of_stars = int(input("Enter number of stars: ").strip())
for i in range(1,number_of_stars + 1):
    print("*", end=' ')
print()

"d. print lines of increasing stars."
line_of_stars = int(input("Enter number of star-lines: ").strip())
for i in range(1, line_of_stars + 1):
    print("*" * i)
print()