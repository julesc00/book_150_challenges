import random


def write_nums_to_file():
    """
    105
    Write a new file called “Numbers.txt”. Add five numbers to the document which are stored on the same line
    and only separated by a comma. Once you have run the program, look in the location where your program is
    stored, and you should see that the file has been created. The easiest way to view the contents of the new text file
    on a Windows system is to read it using Notepad.
    :return:
    """
    with open("docs/numbers.txt", "w") as f:
        nums = []
        for _ in range(1, 5+1):
            num = random.randint(1, 100)
            nums.append(str(num))
            str_nums = ",".join(nums)
        f.write(str_nums)

    return "Done!"


def write_names_to_file():
    """
    106
    Create a new file called “Names.txt”. Add five names to the document, which are stored on separate lines.
    Once you have run the program, look in the location where your program is tored and check that the file has
    been created properly.
    :return:
    """
    with open("docs/names.txt", "w") as f:
        names, counter = [], 5
        while counter:
            names.append(input(f"{counter} to go; Enter a name").title())
            counter -= 1
        f.write("\n".join(names))
        return "Done!"


def display_names():
    """
    107
    Open the names.txt file and display the data in Python.
    :return:
    """
    with open("docs/names.txt", "r") as f:
        print(f.read())
    return ""


def edit_names():
    """
    108
    Open the Names.txt file. Ask the user to input a new name. Add this to the end of the file and
    display the entire file.
    :return:
    """
    with open("docs/names.txt", "a+") as f:
        name = input("Enter another name: ").title()
        f.write("\n" + name)

    with open("docs/names.txt", "r") as f:
        print(f.read())
    return ""


def show_school_menu():
    """
    109
    Display the following menu to the user:
        1) Create a new file
        2) Display the file
        3) Add a new item to the file
        Make a selection 1, 2, or 3:

    Ask the user to enter 1, 2 or 3. If they select anything other than 1, 2 or 3 it should display a suitable error
    message.

    If they select 1, ask the user to enter a school subject and save it to a new file called “Subject.txt”.
    It should overwrite any existing file with a new file.

    If they select 2, display the contents of the “Subject.txt” file.

    If they select 3, ask the user to enter a new subject and save it to the file and then display
    the entire contents of the file.

    Run the program several times to test the options.
    :return:
    """
    print("""
    School Menu
    1) Create a new file
    2) Display the file
    3) Add a new item to the file 
    """)
    sel = int(input("Make a selection 1, 2 or 3: "))
    while sel not in range(1, 3+1):
        sel = int(input("Enter a valid number from 1 to 3: "))
    else:
        if sel == 1:
            subject = input("Enter a new subject: ").title()
            with open("docs/subjects.txt", "w") as f:
                f.write(subject)
        elif sel == 2:
            with open("docs/subjects.txt", "r") as f:
                print(f.read())
        elif sel == 3:
            new_subject = input("Enter a new subject: ").title()
            with open("docs/subjects.txt", "a") as f:
                f.write("\n" + new_subject)
            with open("docs/subjects.txt", "r") as f:
                print(f.read())
    return ""


if __name__ == "__main__":
    print(show_school_menu())
