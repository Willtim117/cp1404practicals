"""files.py"""
# 1 Write code that asks the user for their name

ask_name = str(input("What is your name: "))
open_file = open("name.txt", "w")
print(ask_name, file=open_file)
open_file.close()
print("Done")

# 2 write code that opens "name.txt"
in_file = open("name.txt")
for line in in_file:
    print(f"Hi {line.strip()}!")
in_file.close()

# 3. Create a text file called numbers.txt and save it
