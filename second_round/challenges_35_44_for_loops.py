
def display_name_v1():
    """
    035
    Ask the user to enter their name and then display their name three times.
    """
    name = input("Please enter your name: ")
    for _ in range(3):
        print(name)


def display_name_v2():
    """
    036
    Alter program 035 so that it will ask the use to enter their name and a number and then
    display their name that number of times.
    """
    name = input("Please, enter your name: ")
    num = int(input("Now, enter a number: "))
    for _ in range(num):
        print(name)


def display_name_letters():
    """
    037
    Ask the user to enter their name and display each letter in their name on a separate line.
    """
    name = input("Please, enter your name: ")
    for letter in name:
        print(letter)


def display_name_letters_v2():
    """
    038
    Change program 037 to also ask for a number. Display their name (one letter at a time on each line)
    and repeat this for the number of times they entered.
    """
    name = input("Please, enter your name: ")
    num = int(input("Now, enter a whole number: "))
    for _ in range(num):
        for letter in name:
            print(letter)


def print_times_table():
    """
    039
    Ask the user to enter a number between 1 and 12, and then display the times table for
    that number.
    """
    my_num = int(input("Enter a number from 1 to 12: "))
    for num in range(1, 10+1):
        print(my_num * num)


def count_down():
    """
    040
    Ask for a number below 50 and then count down from 50 to that number, making
    sure you show the number they entered in the output.
    """
    num = int(input("Enter a number below 50: "))
    for x in range(50, num-1, -1):
        print(x)


def display_number_v3():
    """
    041
    Ask the user to enter their name and a number. If the number is less than 10, then
    display their name that number of times; otherwise display the message 'Too high' three times.
    """
    name = input("Enter name: ")
    user_number = int(input("Enter a number: "))
    if user_number < 10:
        [print(name) for _ in range(user_number)]
    else:
        [print("Too high") for _ in range(3)]


def add_numbers() -> int:
    """
    042
    Set a variable called total to 0. Ask the user to enter five numbers and after each input ask them
    if they want that number included. If they do, then add the number to the total. If they don't want
    it included, then don't add it to the total. After they have entered all five numbers, display the total.
    """
    total_to_0 = 0
    for _ in range(5):
        number = int(input("Enter a number: "))
        answer = input("Do you want to add this number to the total?: 'y' or 'n' ").lower()
        if answer == "y":
            total_to_0 += number
    return total_to_0


def count_up_or_down():
    """
    043
    Check book for instructions
    :return:
    """
    direction = input("Do you want to count 'up' or 'down'?: ").lower()
    if direction == "up":
        top_num = int(input("Enter a positive number other than 1: "))
        for number in range(1, top_num+1):
            print(number)
    elif direction == "down":
        below_20_num = int(input("Enter a number below 20: "))
        for number in range(20, below_20_num-1, -1):
            print(number)
    else:
        print("I don't understand")


def check_number_of_guests():
    """
    044
    Check book for instructions
    """
    guests = []
    number_of_guests = int(input("How many people would you like to invite to your party?: "))
    if number_of_guests < 10:
        for num in range(1, number_of_guests+1):
            name = input(f"Enter the name of guest number {num}: ").title()
            guests.append(name)
            print(f"{name} has been invited")
    elif number_of_guests > 10:
        print("Too many people")


if __name__ == "__main__":
    check_number_of_guests()
