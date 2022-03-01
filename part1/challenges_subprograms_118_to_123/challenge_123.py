"""
123

In Python, it is not technically possible to directly delete a record from a .csv file. Instead, you need
to save the file to a temporary list in Python, make the changes to the list and then overwrite the original file
with the temporary list.

Change the previous program to allow you to do this.

Your menu should now look like this:
    1) Add to file
    2) View all records
    3) Delete a record
    4) Quit program
"""

NAMES = []


def print_names() -> None:
    """
    Fill clean list from names.csv file and print the number of items.
    """
    NAMES.clear()
    with open("docs/names.csv", mode="r") as f:
        names = f.read().split("\n")
        [NAMES.append(name) for name in names]
    for val in NAMES:
        try:
            if val == "":
                NAMES.remove("")
        except IndexError:
            print("Not exists")

    if not len(NAMES):
        print("There are no names, please add one: ")
    else:
        print("---List of Names---")
        [print(f"{idx}: {name}") for idx, name in enumerate(NAMES)]


def add_name() -> None:
    """Register a new name entry."""
    name = input("Enter name: ").title()
    NAMES.append(name)
    NAMES.sort()
    with open("docs/names.csv", "w") as f:
        [f.write(name + "\n") for name in NAMES]


def edit_name() -> None:
    """Edit a name."""
    trigger, old_name, new_name = False, "", ""
    while not trigger:
        try:
            name_idx = int(input("Enter name index to edit: "))
            old_name = NAMES[name_idx]
            new_name = input("Enter new name: ").title()
            NAMES[name_idx] = new_name
            NAMES.sort()
            with open("docs/names.csv", "w") as f:
                [f.write(name + "\n") for name in NAMES]
            trigger = True
        except IndexError:
            print("Enter a valid index number.")
    print(f"{old_name} has been changed successfully to {new_name}.")


def delete_name() -> None:
    """Delete a name entry."""
    trigger, del_name = False, ""
    while not trigger:
        name_idx = int(input("Enter a name index to delete: "))
        try:
            del_name = NAMES[name_idx]
            NAMES.pop(name_idx)
            NAMES.sort()
            with open("docs/names.csv", "w") as f:
                [f.write(name + "\n") for name in NAMES]
            trigger = True
        except IndexError:
            print("Enter a valid index number.")
    print(f"{del_name} has been successfully deleted.")


def main() -> None:
    """Main program CLI"""
    print_names()
    trigger = False
    while not trigger:
        print("""
            *** Choose an option ***
                1) Show all names
                2) Add name
                3) Edit name
                4) Delete name
                5) Save to file and Quit
            """)
        option = input("Enter option number: ")
        if option == "1":
            print_names()
        elif option == "2":
            add_name()
        elif option == "3":
            edit_name()
        elif option == "4":
            delete_name()
        elif option == "5":
            with open("docs/names.csv", "w") as f:
                [f.write(name + "\n") for name in NAMES]
            trigger = True
        else:
            print("Enter a valid option")
    print("Bye!")


if __name__ == "__main__":
    main()
