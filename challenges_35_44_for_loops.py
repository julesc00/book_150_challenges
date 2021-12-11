
def print_name_times():
    """
    035
    Ask the user to enter their name and then display their name three times.
    """
    name = input("Enter your name: ")
    [print(name) for _ in range(0, 3)]


def print_name_times_v2():
    """
    036
    Alter program 035 so that it will ask the user to enter their name and a
    number and then display their name that number of times.
    """
    name = input("Entrer votre prenom: ")
    num = int(input("Entrer une chifre: "))
    [print(name) for _ in range(0, num)]


def print_name_chars():
    """
    037
    Ask the user to enter their name and display each letter in their name on a
    separate line.
    """
    name = input("Enter your name: ")
    [print(char) for char in name]


def print_name_chars_v2():
    """
    038
    Change program 037 to also ask for a number. Display their name (one letter
    at a time on each line) and repeat this for the number of times they entered.
    """
    num = int(input("Entrer une chifre: "))
    prenom = input("Entrer ton prenom: ")
    [[print(char) for char in prenom] for _ in range(0, num)]


def print_times_table():
    """
    039
    Ask the user to enter a number between 1 and 12 and then display the
    times table for that number.
    """
    num = int(input("Entrer une chifre entre 1 et 12: "))
    [print(f"{num} x {x} = {num * x}") for x in range(1, 10+1)]


def number_countdown():
    """
    040
    Ask for a number below 50 and then count down from 50 to that number, making sure you show the number
    they entered in the output.
    """
    num = int(input("Entrer une chifre sous 50: "))
    print(f"Entered number: {num}")
    [print(x) for x in range(50, num-1, -1)] if num < 50 else print("Number over 50")


def display_name_check():
    """
    041
    Ask the user to enter their name and a number. If the number is less than 10, then
    display their name that number of times; otherwise display the message “Too high”
    three times.
    """
    prenom = input("Enter your name: ")
    num = int(input("Enter a number: "))
    [print(prenom) for _ in range(num)] if num < 10 else [print("Too high") for _ in range(3)]


def add_to_total_maybe():
    """
    042
    Set a variable called total to 0. Ask the user to enter five numbers and after each input
    ask them if they want that number included. If they do, then add the number to the total.
    If they do not want it included, don’t add it to the total. After they have entered all
    five numbers, display the total.
    """
    total = 0
    idx_counter = 1
    counter = 0
    yes_counter = 0
    trigger = False
    while not trigger:
        if counter != 5:
            num = int(input(f"{idx_counter} Enter a number: "))
            idx_counter += 1
            answer = input("Do you want to add it to the total? ").lower()
            if answer == "yes":
                total += num
                counter += 1
                yes_counter += 1
            elif answer == "no":
                counter += 1
        else:
            trigger = True
    return f"Total: {total}, times added {yes_counter}"


def count_direction():
    """
    043
    Ask which direction the user wants to count (up or down). If they select up, then ask
    them for the top number and then count from 1 to that number. If they select down, ask
    them to enter a number below 20 and then count down from 20 to that number. If they
    entered something other than up or down, display the message “I don’t understand”.
    """
    trigger = True

    while trigger:
        count_dir = input("Which direction do you want to count, up or down?: ").lower()
        if count_dir == "up":
            num = int(input("Enter your top number: "))
            [print(x) for x in range(1, num+1)]
            trigger = False
        elif count_dir == "down":
            num = int(input("Enter a number below 20: "))
            [print(x) for x in range(20, num-1, -1)]
            trigger = False
        else:
            print("I don't understand")


def party_invite():
    """
    044
    Ask how many people the user wants to invite to a party. If they enter a number below
    10, ask for the names and after each name display “[name] has been invited”. If they
    enter a number which is 10 or higher, display the message “Too many people”.
    """
    guests_list = []
    main_trigger = False
    while not main_trigger:
        guests_total = int(input("How many people do you want to invite to the party?: "))
        if guests_total == 0:
            print("Come on! You have to invite at least 1 person.")
        elif guests_total < 10:
            guest_counter = 0
            guests_trigger = False
            guest_idx = 1

            while not guests_trigger:
                if guests_total:
                    guest_name = input(f"Enter name for guest #{guest_idx}: ").title()
                    print(f"{guest_name} has been invited.")
                    guests_list.append(guest_name)
                    guest_counter += 1
                    guest_idx += 1
                    guests_total -= 1
                elif not guests_total:
                    print("Finished registering guests.")
                    guests_str = ", ".join([name for name in guests_list])
                    print(f"The guests for your party are: {guests_str}.")
                    guests_trigger = True
                    main_trigger = True

        else:
            print("Too many people, invite fewer people.")


if __name__ == "__main__":
    party_invite()

