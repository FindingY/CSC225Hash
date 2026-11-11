"""CSC 225 - Simple menu (provided). Run: python main.py"""
from hash_table import HashTable


table = HashTable()

while True:
    print("\nHASH TABLE")
    print("1. Insert a number")
    print("2. Search for a number")
    print("3. Show table")
    print("4. Choose collision method (starts a new table)")
    print("5. Choose hash function (starts a new table)")
    print("6. Exit")
    choice = input("Choice: ")

    if choice == "1":
        try:
            number = int(input("Number: "))
            table.insert(number)
        except ValueError:
            print("Please enter an integer.")
    elif choice == "2":
        try:
            number = int(input("Number: "))
            print("Found" if table.search(number) else "Not found")
        except ValueError:
            print("Please enter an integer.")
    elif choice == "3":
        table.show()
    elif choice == "4":
        print("Choose: linear, quadratic, chaining")
        method = input("Method: ").strip().lower()
        if method in ("linear", "quadratic", "chaining"):
            table = HashTable(method, table.hash_method)
            print("New empty table created.")
        else:
            print("Unknown method.")
    elif choice == "5":
        print("Choose: mod, digit")
        method = input("Hash function: ").strip().lower()
        if method in ("mod", "digit"):
            table = HashTable(table.method, method)
            print("New empty table created.")
        else:
            print("Unknown hash function.")
    elif choice == "6":
        break
    else:
        print("Choose 1 through 6.")
