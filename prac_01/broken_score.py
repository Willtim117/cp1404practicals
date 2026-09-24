
"""
CP1404/CP5632 - Practical
Broken program to determine score status

The intention is that the score must be between 0 and 100 inclusive;
90 or more is excellent; 50 or more is a pass; below 50 is bad.
There is no intention to do any repetition.

"""

while True:
    score = float(input("Enter score: "))

    if score < 0 or score > 100:
        print("Invalid score")
        continue

    if score < 50:
        print("Bad")
    elif 50 <= score < 90:
        print("Passable")
    else:
        print("Excellent")
    break
