#
# simple_array = [[2, 5, 8], [3, 7, 4], [1, 6, 9]]
#
# print(simple_array)
# print(simple_array[1][2])
#
# data_set = {"A": {"x": 54, "y": 82, "z": 91}, "B": {"x": 75, "y": 29, "z": 80}}
#
# print(data_set["A"])
# print(data_set.get("A", ""))
# print(data_set["A"]["y"])
# print(data_set["B"]["y"])
#
# for i in data_set:
#     print(data_set[i]["y"])
import pandas as pd
from copy import deepcopy


def two_d_list(my_list: list) -> list:
    """
    Create the following using a simple 2D list using the standard Python indexing
    :return: nothing
    """
    lst = my_list[:]
    return lst


def show_row_and_col(my_list: list) -> int:
    """
    097
    Using the 2D list from program 096, ask the user to select a row and a column and display that value.
    :return: 2D index item
    """
    lst = my_list[:]
    df, trigger = pd.DataFrame(lst), False
    print(df)
    row = int(input("Select a row number: "))
    col = int(input("Select a column number: "))
    while not trigger:
        while row not in range(0, len(lst)):
            row = int(input("Select a row number: "))
        else:
            while col not in range(0, len(lst[0])):
                col = int(input("Select a column number: "))
            else:
                trigger = True
    return lst[row][col]


def show_row(my_list: list) -> list:
    """
    098
    Using the 2D list from program 096, ask the user which row they would like displayed and display
    just that row. Ask them to enter a new value and add it to the end of the row and display the row
    099 again.
    :return: row item
    """
    lst = my_list[:]
    trigger = False
    for idx, section in enumerate(lst, 1):
        print(f"{idx}: {section}")
    user_selection = int(input("Select a section of the list: "))
    while not trigger:
        while user_selection not in range(0, len(lst)):
            user_selection = int(input("Select a section of the list: "))
        else:
            user_selection -= 1
            trigger = True
    return lst[user_selection]


def edit_row_col_value(my_list: list) -> list:
    """
    099
    Change your previous program to ask the user which row they want displayed. Display that row. Ask which
    column in that row they want displayed and display the value that is held there. Ask the user if they want
    to change the value. If they do, ask for a new value and change the data. Finally, display the whole row again.
    :return: row
    """
    lst = my_list[:]
    df, trigger = pd.DataFrame(lst), False
    print(df)
    row = int(input("Select a row number: "))
    col = int(input("Select a column number: "))
    while not trigger:
        while row not in range(0, len(lst)):
            row = int(input("Select a row number: "))
        else:
            while col not in range(0, len(lst[0])):
                col = int(input("Select a column number:"))
            else:
                trigger = True

    val = lst[row][col]
    edit = input(f"This is your selection: {val}, do you want to edit it 'yes' or 'no'? ")
    if edit.lower() == "yes":
        edit_num = int(input("Enter a number from 0 to 9: "))
        lst[row][col] = edit_num
    return lst[row]


def show_sales(ds: dict) -> str:
    """
    100 and 101
    Create the following using a 2D dictionary showing the sales each person has made in the different
    geographical regions:
    :param ds:
    :return: print data frame table
    """
    for row, col in ds.items():
        print(f"{row} {col}")

    row = input("Enter name to change: ").title()
    col = input("Enter column letter: ").upper()
    temp_vals = input("Enter sales number to change: ")
    vals = [int(val) for val in temp_vals]
    ds[row][col] = vals
    for row, col in ds.items():
        print(f"{row} {col}")

    return ""


def show_user_details():
    """
    102
    Ask the user to enter the name, age and shoe size for four people. Ask for the name of one of the people in
    the list and display their age and shoe size.
    :return:
    """
    users, counter = {}, 4
    while counter:
        name = input(f"{counter} to go; Enter user name: ").title()
        age = int(input("Enter user's age: "))
        shoe_size = float(input("Enter show size: "))
        users[name] = {
            "age": age,
            "show_size": shoe_size
        }
        counter -= 1
    ask_name = input("Enter a name: ").title()
    return users.get(ask_name, "")


def show_user_details2():
    """
    103
    Adapt program 102 to display the names and ages of all the people in the list but do not show their shoe
    size.
    :return: user details without shoe size
    """

    users, counter = {}, 4
    while counter:
        name = input(f"{counter} to go; Enter user name: ").title()
        age = int(input("Enter user's age: "))
        shoe_size = float(input("Enter show size: "))
        users[name] = {
            "age": age,
            "show_size": shoe_size
        }
        counter -= 1

    for name in users:
        print(name, users[name]["age"])
    return ""


def remove_user():
    """
    014
    After gathering the four names, ages and shoe sizes, ask the user to enter the name of the person they want
    to remove from the list. Delete this row from the data and display the other rows on separate lines.
    :return: Print remaining rows, print None.
    """
    users, counter = {}, 4
    while counter:
        name = input(f"{counter} to go; Enter user name: ").title()
        age = int(input("Enter user age: "))
        shoe_size = float(input("Enter user shoe size: "))
        users[name] = {"age": age, "shoe_size": shoe_size}
        counter -= 1

    rm_user = input("Enter user name to remove: ").title()
    # users.pop(rm_user)
    del users[rm_user]  # Different way to remove an item.
    [print(f"{name}, {users[name]['age']}, {users[name]['shoe_size']}") for name in users]

    return ""


if __name__ == "__main__":
    LST = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
    LST2 = [
        [[3, 0, 5, 6], [8, 4, 6, 3], [8, 4, 4, 1], [2, 6, 9, 4]],
        [[4, 8, 3, 2], [6, 7, 8, 6], [4, 7, 3, 7], [3, 6, 1, 2]],
        [[5, 2, 3, 9], [4, 8, 0, 2], [5, 8, 2, 0], [1, 8, 5, 9]],
        [[3, 9, 0, 4], [3, 6, 4, 5], [8, 8, 2, 1], [2, 4, 5, 1]]
    ]
    DATA_SET = {
        "John": {
            "N": [3, 0, 5, 6],
            "S": [8, 4, 6, 3],
            "E": [8, 4, 4, 1],
            "W": [2, 6, 9, 4]
        },
        "Tom": {
            "N": [4, 8, 3, 2],
            "S": [6, 7, 8, 6],
            "E": [4, 7, 3, 7],
            "W": [2, 6, 9, 4]
        },
        "Anne": {
            "N": [5, 2, 3, 9],
            "S": [4, 8, 0, 2],
            "E": [5, 8, 2, 0],
            "W": [1, 8, 5, 9]
        },
        "Fiona": {
            "N": [3, 9, 0, 4],
            "S": [3, 6, 4, 5],
            "E": [8, 8, 2, 1],
            "W": [2, 4, 5, 1]
        }
    }

    print(remove_user())
