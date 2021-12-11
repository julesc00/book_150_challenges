def display_name_length():
    """
    020
    Ask the use to enter their first name and then display the length of
    their name.
    """
    name = input("Enter your name: ")
    return f"Your name has {len(name)} letters."


def join_full_name():
    """
    021
    Ask the user to enter their first name and then ask them to
    enter their surname. Join them together with a space between
    and display the name and the length of whole name.
    """
    name_lst = []
    name = input("Enter your first name: ").title()
    last_name = input("Enter your last name: ").title()
    name_lst.append(name)
    name_lst.append(last_name)
    full_name = " ".join(name_lst)
    print(full_name)

    return f"Your full name is: {full_name} and contains {len(name + last_name)} characters."


def get_full_name_then_titled():
    """
    022
    Ask the user to enter their first name and surname in lower case.
    Change the case to title case and join them together.
    Display the finished result.
    """
    full_name = input("Enter your full name: ").title()
    return full_name


def ask_for_rhyme_display_indices():
    """
    023
    Ask the user to type in the first line of a nursery rhyme and display
    the length of the string. Ask for a starting number and an ending number
    and then display just that section of the text(remember Python starts
    counting from 0 and not 1).
    """
    rhyme = input("Enter your favorite nursery rhyme: ")
    num1 = int(input(f"Enter a starting number from 1 to {len(rhyme)}: "))
    num2 = int(input("Enter an ending number: "))
    section = rhyme[num1+1:num2]

    return section


if __name__ == "__main__":
    print(ask_for_rhyme_display_indices())
