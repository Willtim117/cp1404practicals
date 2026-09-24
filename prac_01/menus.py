"""Enter name: Guido
(H)ello
(G)oodbye
(Q)uit
A
Invalid choice
(H)ello
(G)oodbye
(Q)uit
H
Hello Guido
(H)ello
(G)oodbye
(Q)uit
 Q
Finished."""


get_name = input("Enter Name: ").strip().upper()
menu = """(H)ello
(G)oodbye
(Q)uit"""

print(menu)
choice = input(">>> ").upper()

while choice != "Q":
    if choice == "H":
        print(f"Hello {get_name}")
    elif choice == "G":
        print(f"Goodbye {get_name}")
    else:
        print("Invalid Choice")
    print(menu)
    choice = input(">>> ").upper()
print("Finished.")





