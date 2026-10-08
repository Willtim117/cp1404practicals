import random

# Constants
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6


def main():
    """Gets and generates the number of picks where each pick consists of random numbers
        in ascending order."""
    num_quick_picks = int(input("How many quick picks? "))

    for i in range(num_quick_picks):
        quick_pick = generate_quick_pick(NUMBERS_PER_PICK)

        print(" ".join(f"{str(number):>2}" for number in sorted(quick_pick)))


def generate_quick_pick(numbers_per_pick: int) -> list:
    """Get amount numbers in a quick pick then generates the quick pick: unique random numbers sorted ascending."""
    quick_pick = []
    while len(quick_pick) < numbers_per_pick:
        random_int = random.randint(MIN_NUMBER, MAX_NUMBER)
        if random_int not in quick_pick:
            quick_pick.append(random_int)
    return quick_pick


main()
