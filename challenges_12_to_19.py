"""
If Statements section
"""

# Example code

num = 13
if num > 10:
    print("It's over 10")
else:
    print("It's not over 10")

if num > 10:
    print("This is over 10")
elif num == 10:
    print("it's equal to 10")
else:
    print("It's under 10")

if num >= 10:
    if num <= 20:
        print("this is between 10 and 20")
    else:
        print("This is over 20")
else:
    print("This is under 10")


def num_checker():
    num2 = int(input("Enter a number between 10 and 20: "))

    if num2 >= 10 and num2 <= 20:
        print("Thank you!")
    else:
        print("Out of range.")


def even_checker():
    num2 = int(input("Enter an even number between 1 and 5: "))
    if num2 == 2 or num == 4:
        print("Thank you!")
    else:
        print("Incorrect!")


def show_smallest_num_first():
    """
    012
    Ask for two numbers. If the first one is larger than the second, display
    the second number first and then the first  number, otherwise show
    the first number first and  then the second.
    """
    nums = []
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a different number: "))
    nums.append(num1)
    nums.append(num2)

    sorted_list = sorted(nums)
    for n in sorted_list:
        print(n)


def show_num_under_twenty():
    """
    013
    Ask the user to enter a number that is under 20. If they enter a
    number that is 20 or more, display the message “Too high”, otherwise display
    “Thank you”.
    """
    num1 = int(input("Enter a number below 20: "))
    if num1 >= 20:
        print("Too high")
    else:
        print("Thank you")


def show_num_within_range():
    """
    014
    Ask the user to enter a number between 10 and 20 (inclusive).
    If they enter a number within this range, display the message “Thank
    you”, otherwise display the message “Incorrect answer”.
    """
    num1 = int(input("Enter a number between 10 and 20: "))
    if num1 >= 10 and num1 <= 20:
        print("Thank you")
    else:
        print("Incorrect answer!")


def display_fav_color():
    """
    015
    Ask the user to enter their favourite colour. If they enter “red”, “RED” or
    “Red” display the message “I like red too”, otherwise display the message
    “I don’t like [colour], I prefer red”.
    """
    fav_color = input("Enter your favorite color: ").lower()
    if fav_color == "red":
        print("I like red too.")
    else:
        print(f"I don't like {fav_color}, I prefer red.")


def rainy_or_windy():
    """
    016
    Ask the user if it is raining and convert their answer to lower case so it doesn’t matter what case they
    type it in. If they answer “yes”, ask if it is windy. If they answer “yes” to this second question,
    display the answer “It is too windy for an umbrella”, otherwise display the message “Take an umbrella”.
    If they did not answer yes to the first question, display the answer “Enjoy your day”.
    """
    is_rainy = input("Is it rainy today? ").lower()

    if is_rainy == "yes":
        is_windy = input("Is it windy?").lower()
        if is_windy == "yes":
            print("It is too windy for an umbrella")
        else:
            print("Take an umbrella")
    else:
        print("Enjoy your day.")


def do_according_to_age():
    """
    017
    Ask the user’s age. If they are 18 or over, display the message “You can vote”, if  they are aged 17, display the
    message “You can learn to drive”, if they are 16, display the message “You can buy a  lottery ticket”, if they
    are under 16, display the message “You can go Trickor-Treating”.
    """
    age = int(input("What is your age?: "))
    if age >= 18:
        print("You can vote")
    elif age == 17:
        print("You can learn to drive.")
    elif age == 16:
        print("You can buy a lottery ticket.")
    else:
        print("Go play with your toys.")


def display_number_msg():
    num1 = int(input("Enter a number: "))
    if num1 < 10:
        print("Too low")
    elif 10 <= num1 <= 20:
        print("Correct")
    else:
        print("Too high")


def display_msg_1_2_or_3():
    num1 = int(input("Enter 1 or 2 or 3: "))
    if num1 == 1:
        print("Thank you")
    elif num1 == 2:
        print("Well done")
    elif num1 == 3:
        print("Correct")
    else:
        print("Error message!")


if __name__ == "__main__":
    display_msg_1_2_or_3()





