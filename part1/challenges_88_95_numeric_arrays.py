import random
from array import *

# nums = array("i", [2, 3, 5, 6])
# print(type(nums))
#
# for n in nums:
#     print(n)


def show_reversed_array():
    """
    088
    Ask the user for a list of five integers. Store them in an array.
    Sort the list and display it in reverse order.
    """
    counter, nums = 5, array("i")
    while counter:
        nums.append(int(input(f"{counter} numbers to go: Enter a number: ")))
        counter -= 1
    return sorted(nums, reverse=True)


def random_array():
    """
    089
    Create an array which will store a list of integers. Generate five random numbers and store them in
    the array. Display the array (showing each item on a separate line).
    """
    import random
    rand_array, counter = array("i"), 5
    while counter:
        rand_array.append(random.randint(1, 1000))
        counter -= 1
    for num in rand_array:
        print(num)
    return ""


def show_nums():
    """
    090
    Ask the user to enter numbers. If they enter a number between 10 and 20, save it in the array,
    otherwise display the message “Outside the range”. Once five numbers have been
    successfully added, display the message “Thank you” and display the array with each item shown
    on a separate line.
    """
    counter, num_array = 5, array("i")
    while counter:
        num = int(input("Enter a number between 10 and 20: "))
        if 10 < num < 20:
            num_array.append(num)
            counter -= 1
        else:
            print("Outside the range.")
    return "Thank you"


def show_num_times():
    """
    091
    Create an array which contains five numbers (two of which should be repeated). Display
    the whole array to the user. Ask the user to enter one of the numbers from the array and
    then display a message saying how many times that number appears in the list.
    :return: the times a number appears in the array.
    """
    arr = [1, 2, 3, 5, 5]
    print(arr)
    user_num = int(input("Enter one of the numbers from the array: "))
    arr.append(user_num)
    count = arr.count(user_num)
    return f"{user_num} appears {count} times in the array."


def joined_arrays():
    """
    092
    Create two arrays (one containing three numbers that the user enters and one containing a set of five random
    numbers). Join these two arrays together into one large array.
    Sort this large array and display it so that each number appears on a separate line.
    :return: the joined long array
    """
    arr, rand_arr, trigger = array("i"), array("i"), 3
    for _ in range(1, 5+1):
        rand_arr.append(random.randint(1, 100))
    while trigger:
        arr.append(int(input(f"{trigger} to go; Enter a number: ")))
        trigger -= 1

    merged_arr = sorted(arr + rand_arr)
    return merged_arr


def show_nums_to_user():
    """
    Ask the user to enter five numbers. Sort them into order and present them to the user.
    Ask them to select one of the numbers. Remove it from the original array and save it in a
    new array.
    :return: new array with one item.
    """
    arr, trigger = [], 5
    while trigger:
        arr.append(int(input(f"{trigger} to go; Enter a number: ")))
        trigger -= 1
    arr.sort()

    print(f"Choose a number from your array: {arr}")
    tmp = int(input("Enter the number to be removed: "))
    popped, new_array = 0, []

    for idx, num in enumerate(arr):
        if tmp == num:
            popped = arr.pop(idx)
            new_array.append(popped)

    return new_array


if __name__ == "__main__":
    print(show_nums_to_user())
