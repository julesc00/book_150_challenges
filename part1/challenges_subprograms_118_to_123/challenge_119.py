"""
119

Define a subprogram that will ask the user to pick a low and a high number, and then generate a random
number between those two values and store it in a variable called “comp_num”.

Define another subprogram that will give the instruction “I am thinking of a number…” and then ask the user to
guess the number they are thinking of.

Define a third subprogram that will check to see if the comp_num is the same as the user’s guess. If it is,
it should display the message “Correct, you win”, otherwise it should keep looping, telling the user if they are
too low or too high and asking them to guess again until they guess correctly.
"""
from random import randint


def get_random_num() -> int:
    """Generate a random number from low-high user input numbers."""
    low_num = int(input("Enter a low number between 1 to 10: "))
    high_num = int(input("Enter a high number between 1 to 10: "))
    rand_num = randint(low_num, high_num)
    print(f"Random number: {rand_num}")
    return rand_num


def get_guessed_num() -> int:
    """Get user guessed number."""
    print("I am thinking of a number...")
    user_num = int(input("What number am I thinking of?: "))
    return user_num


def check_num():
    """Check in get_random_num return == to get_guessed_num return."""
    rand_num = get_random_num()
    trigger = False
    while not trigger:
        user_num = get_guessed_num()
        if rand_num == user_num:
            print("Correct, you win!")
            trigger = True
        else:
            if user_num < rand_num:
                print("Too low!")
            elif user_num > rand_num:
                print("Too high!")

    return ""


if __name__ == "__main__":
    print(check_num())
