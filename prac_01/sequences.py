menu = """
1. Show the even numbers from x to y
2. Show the odd numbers from x to y
3. Show the squares of the numbers from x to y (e.g., if x, y = 2, 4 then: 4 9 16)
4. Exit the program
"""

get_X = int(input("Enter X: ").strip().upper())
get_Y = int(input("Enter Y: ").strip().upper())

if get_Y < get_X:
    print("Y must be greater than X")
    get_Y = int(input("Enter Y: ").strip().upper())

# --------------------------
print(menu)
while True:
    try:
        get_option = int(input("Enter Option: ").strip())
        if get_option == 1:
            for i in range(get_X, get_Y + 1):
                if i % 2 == 0:
                    print(i, end=' ')
            print()
        elif get_option == 2:
            for i in range(get_X, get_Y + 1):
                if i % 2 != 0:
                    print(i, end=' ')
            print()
        elif get_option == 3:
            for i in range(get_X, get_Y + 1):
                print(i ** 2, end=' ')
            print()
        elif get_option == 4:
            break
        else:
            print("Invalid Choice")
    except ValueError:
        print("Invalid Choice. Please enter 1,2,3 or 4")

    print(menu)
#  get_option = int(input("Enter Option: ").strip())

print("Finished.")
