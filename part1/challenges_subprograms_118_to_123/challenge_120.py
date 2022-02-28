"""
120
Display the following menu to the user:
    1) Addition
    2) Subtraction
    Enter 1 or 2:

If they enter a 1, it should run a subprogram that will generate two random numbers between 5 and 20, and ask the
user to add them together. Work out the correct answer and return both the user’s answer and the correct answer.

If they entered 2 as their selection on the menu, it should run a subprogram that will generate one number between
25 and 50 and another number between 1 and 25 and ask them to work out num1 minus num2. This way they will not have
to worry about negative answers. Return both the user’s answer and the correct answer.

Create another subprogram that will check if the user’s answer matches the actual answer. If it does, display
“Correct”, otherwise display  a message that will say “Incorrect, the answer is” and display the real answer.

If they do not select a relevant option on the first menu you should display a suitable message.
"""
from random import randint


def get_addition() -> dict:
    """Addition results and user's."""
    num1, num2 = randint(5, 20), randint(5, 20)
    result = num1 + num2
    user_result = int(input(f"Add {num1} + {num2} = "))
    results = {"result": result, "user_result": user_result}
    return results


def get_subtraction() -> dict:
    """Subtraction results and user's."""
    num1, num2 = randint(5, 20), randint(5, 20)
    result = max(num1, num2) - min(num1, num2)
    user_result = int(input(f"Subtract {max(num1, num2)} - {min(num1, num2)} = "))
    results = {"result": result, "user_result": user_result}
    return results


def check_results() -> str:
    """Check if result equals that of the user."""
    trigger = False
    while not trigger:
        print("""
            1) Addition
            2) Subtraction
            Enter 1 or 2:
        """)
        selection = input("Enter a number: ")
        if selection == "1":
            addition = get_addition()
            if addition["result"] == addition["user_result"]:
                print("Correct!")
            else:
                print(f"Incorrect result, yours: {addition['user_result']} is not {addition['result']}")
            trigger = True
        elif selection == "2":
            subtraction = get_subtraction()
            if subtraction["result"] == subtraction["user_result"]:
                print("Correct!")
            else:
                print(f"Incorrect result, yours: {subtraction['user_result']} is not {subtraction['result']}")
            trigger = True
        else:
            print("Please, enter a valid option")
    return ""


if __name__ == "__main__":
    print(check_results())
