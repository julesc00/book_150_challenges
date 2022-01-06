import random


def exercise1():
    num = random.random()
    num *= 100
    print(num)


def exercise_random_int():
    return random.randint(0, 9)


def exercise_random_divider():
    n1 = random.randint(0, 1000)
    n2 = random.randint(0, 1000)
    return n1 / n2


def exercise_random_range():
    return random.randrange(0, 100, 5)


def exercise_random_color_picker():
    return random.choice(["red", "black", "green"])


def rand_int():
    """
    052
    Display a random integer between 1 and 100 inclusive.
    """
    return random.randrange(1, 100)


def rand_fruit():
    """
    053
    Display a random fruit from a list of five fruits.
    """
    fruits = ["banana", "mango", "pear", "orange", "lemon"]
    return random.choice(fruits)


def heads_or_tails() -> str:
    """
    054
     Randomly choose either heads or tails (“h” or “t”). Ask the user to
     make their choice. If their choice is the same as the randomly
     selected value, display the message “You win”, otherwise display
     “Bad luck”. At the end, tell the user if the computer selected heads
     or tails.
    """
    coin_sides = ("h", "t")
    user_pick = input("'h' or 't'?: ")
    rand_select = random.choice(coin_sides)
    if user_pick in rand_select:
        print("You win!")
    else:
        print("You lose :(")
    return f"Computer choice was: {rand_select}"


def rand_num_choice() -> str:
    """
    055
     Randomly choose a number between 1 and 5. Ask the user to pick a number. If they guess
     correctly, display the message “Well done”, otherwise tell them if they are too high or
     too low and ask them to pick a second number. If they guess correctly on their second
     guess, display “Correct”, otherwise display “You lose”.
    """
    rand_num = random.choice(range(1, 5 + 1))
    trigger, user_pick = 2, 0

    while trigger:
        if user_pick < rand_num or user_pick > rand_num:
            user_pick = int(input("Pick a number from 1 to 5: "))
            trigger -= 1
            if user_pick == rand_num:
                print(f"Computer choice: {rand_num}")
                return "Well done!"
            elif trigger == 1 and user_pick == rand_num:
                print(f"Computer choice: {rand_num}")
                return "Correct"
    print(f"Computer choice: {rand_num}")
    return "You lose"


def choose_rand_num():
    """
    056
     Randomly pick a whole number between 1 and 10. Ask the user to enter a number and
    keep entering numbers until they enter the number that was randomly picked.
    """
    rand_num = random.choice(range(1, 10 + 1))
    user_pick = 0
    while user_pick != rand_num:
        user_pick = int(input("Enter a number from 1 to 10: "))
    return ""


def choose_rand_num2():
    """
    057
    Update program 056 so that it tells the use if they are too high or too low before
    they pick  again.
    """
    rand_num = random.choice(range(1, 10 + 1))
    user_pick = 0
    while user_pick != rand_num:
        user_pick = int(input("Enter a number from 1 to 10: "))
        print("Too low") if user_pick < rand_num else print("Too high")
    return ""


def random_math_quiz() -> str:
    """
    058
    Make a maths quiz that asks five questions by randomly generating two whole numbers to make the question
    (e.g. [num1] + [num2]). Ask the user to enter the answer. If they get it right add a point to their score. At
    the end of the quiz, tell them how many they got correct out of five.
    """
    trigger, score = 5, 0
    while trigger:
        n1, n2 = int(random.choice(range(1, 1000))), int(random.choice(range(1, 1000)))
        result = n1 + n2
        user_answer = int(input(f"[{n1}] + [{n2}]: "))
        if user_answer and user_answer == result:
            score += 1
        trigger -= 1

    return f"Your score {score}"


def choose_color() -> str:
    """
    059
    Display five colours and ask the user to pick one. If they
    pick the same as the program has chosen, say “Well done”, otherwise display a witty answer which involves
    the correct colour, e.g. “I bet you are GREEN with envy” or “You are probably feeling BLUE right now”. Ask
    them to guess again; if they have still not got it right, keep giving them the same clue and ask the user to
    enter a colour until they guess it correctly.
    """
    colors = ("RED", "BLUE", "GREEN", "PINK", "ORANGE")
    user_pick, computer_pick = "", random.choice(colors)
    while user_pick != computer_pick:
        user_pick = input(f"Choose a color: {', '.join(colors)} ").upper()
        computer_pick = random.choice(colors)
        print(f"You're feeling {computer_pick}") if user_pick != computer_pick else ""

    return "you got it!"


if __name__ == "__main__":
    print(choose_color())
