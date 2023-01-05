import time


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


def guest_invite_checker() -> str:
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
    trigger = False
    guests.append(name)
    print(f"{name} a été invité.")
    while not trigger:
        invite = input(f"Vous aimeriez inviter quelqu'un plus? ").lower()
        if invite == "oui":
            name2 = input("Comment ce-que s'appelle votre invité? ").title()
            guests.append(name2)
            print(f"{name2} a été invité.")
            count += 1
        else:
            trigger = True
    return f"Vous avez invité {count} invités. Ses invités sont: {', '.join(guests)}."


def guess_num() -> str:
    """
    049
    Create a variable called comp_num and set the value to 50. Ask the user to enter a number. While their guess
    is not the same as the comp_num value, tell them if their guess is too low or too high and ask them to have
    another guess. If they enter the same value as comp_num, display the message “Well done, you took [count] attempts”.
    """
    comp_num = 50
    guess = int(input("Entrer une chifre: "))
    attempts = 1
    while guess != comp_num:
        guess = int(input("Was your guess too high or too low? Enter another number: "))
        attempts += 1
    return f"Well done you took {attempts} attempts."


def guess_to_high_too_low() -> str:
    """
    050
    Ask the user to enter a number between  10 and 20. If they enter a value under 10,  display the message “Too low”
    and ask them to try again. If they enter a value above 20, display the message “Too high” and ask them to try again.
    Keep repeating this until they enter a value that is between 10 and 20 and then display the message “Thank you”.
    """
    val = int(input("Enter a number between 10 and 20: "))
    trigger = False
    while not trigger:
        if 10 <= val <= 20:
            trigger = True
            return "Thank you!"
        elif val < 10:
            val = int(input("Too low! Enter another number between 10 and 20: "))
        elif val > 20:
            val = int(input("Too high! Enter another number between 10 and 20: "))


def green_bottles_game() -> str:
    """
    051
    Using the song “10 green bottles”, display the lines “There are [num] green bottles hanging on the wall, [num]
    green bottles hanging on the wall, and if 1 green bottle should accidentally fall”. Then, ask “how many green
    bottles will be hanging on the wall?” If the user answers correctly, display the message “There will be
    [num] green bottles hanging on the wall”. If they answer incorrectly, display the message “No, try again” until
    they get it right. When the number of green bottles getsdown to 0, display the message “There are no more green
    bottles hanging on the wall”.

    Used time module to mimic and give time for message reading.
    """
    qty = 10
    trigger = False
    while not trigger:
        if not qty:
            trigger = True
            return f"There are no more green bottles hanging on the wall."
        else:
            print(f"There are {qty} green bottles hanging on the wall,")
            time.sleep(2)
            print(f"{qty} green bottles hanging on the wall, if 1 green bottle should accidentally fall.")
            time.sleep(2)
            qty -= 1
            val = int(input("How many green bottles will be hanging on the wall? "))
            if val == qty:
                trigger = True
                time.sleep(1)
                return f"There will be {qty} hanging on the wall."

            else:
                print("No, try again")


if __name__ == "__main__":
    print(green_bottles_game())
