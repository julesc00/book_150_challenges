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
    section = rhyme[num1 + 1:num2]

    return section


def to_all_caps():
    """
    024
    Ask the user to type in any word and display it in upper case.
    """
    any_str = input("Enter whatever: ").upper()
    return any_str


def first_name_check():
    """
    025
    Ask the user to enter their first name. If the length of their first
    name is under five characters, ask  them to enter their surname and
    join them together (without a space) and display the name in upper case.
    If the length of the first name is five or more characters, display
    their first name in lower case.
    """
    name_list = []
    first_name = input("Enter your first name: ")
    if len(first_name) >= 5:
        last_name = input("Enter your last name: ")
        name_list.append(first_name)
        name_list.append(last_name)
        full_name = "".join(name_list)

        return full_name.upper()
    else:
        return first_name.lower()


def pig_latin():
    """
    026
    Pig Latin takes the first consonant of a word, moves it to the end of the word and adds on an “ay”.
    If a word begins with a vowel you just add “way” to the end. For example, pig becomes igpay, banana becomes
    ananabay, and aadvark becomes aadvarkway. Create a program that will ask the user to enter a word and change it
    into Pig Latin. Make sure the new word is displayed in lower case.
    """
    word = input("Enter a word: ").lower()
    vowels = "aeiou"
    if word[0] in vowels:
        return word + "way"
    else:
        char2, temp_word = word[0], word[1:]
        return temp_word + char2 + "ay"


if __name__ == "__main__":
    print(pig_latin())
