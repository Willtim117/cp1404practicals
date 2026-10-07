
def main():
    """Get 5 numbers and display information."""
    numbers = []

    for i in range(5):
        get_number = int(input(f"Number: "))
        numbers.append(get_number)

    average = sum(numbers)/len(numbers)

    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {average}")


main()

