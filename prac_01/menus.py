"""
GET name
DISPLAY menu
GET choice
WHILE choice != Q
    IF choice == H
        DISPLAY "hello" name
    ELSE IF choice == G
        DISPLAY "goodbye" name
    ELSE
        DISPLAY invalid message
    DISPLAY menu
    GET choice
DISPLAY finished message
"""

name = input("Enter name: ")

def display_menu():
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")

display_menu()
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    display_menu()
    choice = input(">>> ").upper()

print("Finished.")