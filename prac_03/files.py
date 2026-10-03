"""files.py"""
# 1 Write code that asks the user for their name

ask_name = str(input("What is your name: "))
name_file = open("name.txt", "w")
print(ask_name, file=name_file)
name_file.close()
print("Done")

# 2 write code that opens "name.txt"
in_file = open("name.txt")
for line in in_file:
    print(f"Hi {line.strip()}!")
in_file.close()

# 3. Create a text file called numbers.txt and save it
with open("numbers.txt", "r") as numbers_file:
    sum_numbers = 0
    total_numbers = 0

    for i, line in enumerate(numbers_file):
        # Summing a definite number of lines
        if i < 4:
            sum_numbers += int(line)
        # Summing all the lines
        total_numbers += int(line)

    print(f"Summation: {sum_numbers}")
    print(f"Total: {total_numbers}")


# 4 Now write a fourth block of code that prints the total for all lines
"4. refactored in code above."
