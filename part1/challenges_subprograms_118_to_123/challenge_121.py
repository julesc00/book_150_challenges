"""
121
    *** Choose an option ***
    1) Show all names
    2) Add name
    3) Edit name
    4) Delete name
    5) Quit

Create a program that will allow the user to easily manage a list of names.

You should display a menu that wil allow them to add a name to the list, change a name in the list, delete a name
from the list or view all the names in the list.

There should also be a menu option to allow the user to end the program. If they select an option that is not
relevant, then it should display a suitable message. After they have made a selection to either add a name, change a
name, delete a name or view all the names, they should see the menu again without having to restart the program.

The program should be made as easy to use as possible.
"""


NAMES = []


def add_name() -> None:
    """Register a new name entry."""
    name = input("Enter name: ").title()
    NAMES.append(name)
    NAMES.sort()


def print_names() -> None:
    print("---List of Names---")
    if not len(NAMES):
        print("There are no names, please add one: ")
    else:
        for idx, name in enumerate(NAMES):
            print(f"{idx}: {name}")


def edit_name() -> None:
    """Edit a name."""
    print_names()
    trigger, old_name, new_name = False, "", ""

    while not trigger:
        try:
            name_idx = int(input("Enter name index to edit: "))
            old_name = NAMES[name_idx]
            new_name = input("Enter new name: ").title()
            NAMES[name_idx] = new_name
            NAMES.sort()
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
                5) Quit
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
            trigger = True
        else:
            print("Enter a valid option")
    print("Bye!")


if __name__ == "__main__":
    main()
