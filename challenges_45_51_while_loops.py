
def count_to_50():
    """
    045
    Set the total to 0 to start with. While the total is 50 or less, ask
    the user to input a number. Add that number to the total and print the
    message “The total is… [total]”. Stop the loop when the total is over 50.
    """
    total = 0
    while total <= 50:
        num = int(input("Input a number: "))
        total += num
        print("The total is: ", total)


def display_last_num():
    """
    046
    Ask the user to enter a number. Keep asking until they enter a value
    over 5 and then display the message “The last number you entered was
    a [number]” and stop the program.
    """
    trigger = 0
    while trigger <= 5:
        num = int(input("Enter a number: "))
        trigger = num
    print(f"Your last number was: {trigger}")


def keep_adding_nums():
    """
    047
    Ask the user to enter a number and then enter another number. Add these two numbers together and
    then ask if they want to add another number. If they enter “y", ask them to enter another number and
    keep adding numbers until they do not answer “y”. Once the loop has stopped, display the total.
    """
    num1 = int(input("Entrer une chifre: "))
    num2 = int(input("Entrer un'autre chifre: "))
    total = num1 + num2
    trigger = False
    while not trigger:
        answer = input("Voulez-vous entrer un'autre chifre?: ")
        if answer == "y":
            num_x = int(input("Entrer un'autre chifre: "))
            total += num_x
        else:
            trigger = True
    return f"Total: {total}"


def guest_invite_checker():
    """
    048
    Ask for the name of somebody the user wants to invite to a party. After this, display the message
    “[name] has now been invited” and add 1 to the count. Then ask if they want to invite somebody else.
    Keep repeating this until they no longer want to invite anyone else to the party and then display
    how many people they have 049 coming to the party.
    """
    name = input("Comment ce-que s'appelle votre invité? ").title()
    count = 1
    guests = []
    final_msg = {}
    trigger = False
    guests.append(name)
    print(f"{name} a été invité.")
    while not trigger:
        invite = input(f"Vous aimeriez inviter quelqu'une plus? ").lower()
        if invite == "oui":
            name2 = input("Comment ce-que s'appelle votre invité? ").title()
            guests.append(name2)
            print(f"{name2} a été invité.")
            count += 1
        else:
            trigger = True
    return f"Vous avez invité {count} invités. Ses invités sont: {', '.join(guests)}."


if __name__ == "__main__":
    print(guest_invite_checker())
