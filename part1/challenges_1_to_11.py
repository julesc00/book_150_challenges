
def display_firstname():
    """
    001
    Ask for the user's first name and display the output message.
    """
    firstname = input("Enter your firstname: ")
    return f"Hello {firstname.title()}"


def display_fullname():
    """
    002
    Ask for the user's firstname and then ask for their lastname/surname and display the output
    message: Hello [Firstname] [Lastname]
    """
    firstname = input("Enter your firstname: ")
    lastname = input("Now, enter your lastname: ")

    return f"Hello {firstname.title()} {lastname.title()}."


def display_joke():
    """
    003
    Write code that will display the joke 'What do you call a bear with no teeth?' and on the next line
    display the anser 'A gummy bear!'. Try not to create it using only one line of code.
    """
    question = "What do you call a bear with no teeth?\n"
    answer = "A gummy bear!"

    return question + answer


def sum_nums(x: int, y: int):
    """
    004
    Ask the user to enter two numbers. Add them together and display the answer as 'The total is <answer>'.
    """
    return f"The total is {x + y}"


print(sum_nums(10, 20))


def sum_mult_nums(x: int, y: int, z: int) -> str:
    """
    005
    Ask the user to enter three numbers. Add together the first two numbers and then multiply this total
    by the third. Display the answer as 'The answer is <answer>.
    """
    result = (x + y) * z
    return f"The answer is {result}."


def left_pizza_slices():
    """
    005
    Ask how many slices of pizza the user started with and ask how many slices they have eaten. Work out
    how many slices they have left and display the answer in a user-friendly format.
    """
    initial_pizzas = int(input("How pizza slices did you start with?: "))
    slices_left = int(input("How many slices have you eaten so far?: "))
    if initial_pizzas < 1:
        initial_pizzas = int(input("Don't lie, enter a valid number: "))
        slices_left = int(input("How many slices have you eaten so far?: "))
        left_total = initial_pizzas - slices_left
        print(f"You have {left_total} slices.")
    else:
        left_total = initial_pizzas - slices_left
        print(f"You have {left_total} slices.")


def tell_birthday_age():
    """
    007
    Ask the user for their name and their age. Add 1 to their age and display the output: <name> next
    birthday you'll be <age>.
    """
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    while age <= 0:
        age = int(input("Enter your age!: "))
    else:
        print(f"{name.title()} next birthday you will be {age + 1}.")


def bill_divided_equally():
    """
    008
    Ask for the total price of the bill, then ask how many diners there are. Divide tht total bill by the number
    of diners and show how much each person must pay.
    """
    bill = float(input("How much is the bill?: "))
    diners = int(input("How many diners are we?: "))
    total_per_diner = float(bill / diners)

    print(f"Each person must pay ${total_per_diner:.2f}")


def days_to_hrs_min():
    """
    009
    Write a program that will ask for a number of days and then will show how many hours, minutes and seconds
    are in that number.
    """
    days = int(input("Enter a number of days: "))
    hours = 24 * days
    minutes = hours * 60
    seconds = minutes * 60

    while days <= 0:
        days = int(input("Enter a valid number of days!: "))
    else:
        print(f"In {days:,} days, there {hours:,} hours, {minutes:,} minutes and {seconds:,} seconds!")


def kilos_to_pounds():
    """
    010
    There are 2.204 pounds in 1 kilo. Ask the user to enter a weight in kilograms and convert it to pounds.
    """
    weight_kilos = float(input("Enter your weight in kilos: "))
    pound = 2.204
    while weight_kilos <= 0:
        weight_kilos = float(input("Enter a valid weight in kilos!: "))
    else:
        user_weight_kilos = float(weight_kilos * pound)
        print(f"Your weight in kilos is: {user_weight_kilos:.2f} pounds.")


def small_num_in_large_num():
    """
    011
    Task the user to enter a number over 100 an then enter a number under 10 and tell them how many times the
    smaller number goes into the larger number in a user-friendly format.
    """
    num1 = int(input("Enter a number over a 100: "))
    while num1 < 100:
        num1 = int(input("Please, enter a number over a 100!: "))
    else:
        num2 = int(input("Enter a number under 10: "))
        while num2 > 10:
            num2 = int(input("Please, Enter a number under 10!: "))
        else:
            result = round(num1 / num2)
            print(f"Number {num2} fits {result} in {num1}.")


if __name__ == "__main__":
    small_num_in_large_num()



