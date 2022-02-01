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


if __name__ == "__main__":
    LST = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
    print(edit_row_col_value(LST))
