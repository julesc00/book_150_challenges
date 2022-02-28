"""
122
Create the following menu:
    1) Add to file
    2) View all records
    3) Quit program

    Enter the number of your selection:

If the user selects 1, allow them to add to a file called Salaries.csv which will store their name
and salary. If they select 2 it should display all records in the Salaries.csv file. If they select 3 it
should stop the program. If they select an incorrect option they should see an error message. They should
keep returning to the menu until they select option 3.
"""


def add_to_file():
    """Add a new employee name and salary entry to file."""
    name = input("Enter your full name: ").title()
    salary = input("Enter your monthly salary in whole numbers: ")

    # Save data to salaries.csv
    with open("docs/salaries.csv", "a") as f:
        f.write(name + ", " + salary + "\n")

    print("Data saved to file.")


def view_all_records():
    """View all entries in salaries.csv"""
    with open("docs/salaries.csv", "r") as f:
        lines = f.read().split("\n")
        for line in lines:
            print(line)


def main_func():
    """Main program for employee name and salary registration."""

    trigger = False
    while not trigger:
        print("""
                Enter the number of your selection:
                    1) Add to file
                    2) View all records
                    3) Quit
                """)
        selection = input("Enter number: ")
        if selection == "1":
            add_to_file()
        if selection == "2":
            view_all_records()
        if selection == "3":
            trigger = True
    return "bye!"


if __name__ == "__main__":
    print(main_func())
