import random

# Constants
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6


def main():
    """Gets and generates the number of picks where each pick consists of 6 random numbers
        between 1 and 45 in ascending order."""
    num_quick_picks = int(input("How many quick picks? "))

    for i in range(num_quick_picks):
        quick_pick = []
        while len(quick_pick) < NUMBERS_PER_PICK:
            random_int = random.randint(MIN_NUMBER, MAX_NUMBER)
            if random_int not in quick_pick:
                quick_pick.append(random_int)

        print(" ".join(f"{str(number):2}" for number in sorted(quick_pick)))


main()
