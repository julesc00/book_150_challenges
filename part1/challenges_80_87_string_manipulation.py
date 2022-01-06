
def display_fullname_len():
    """
    080
    Ask the user to enter their first name and then display the length of their first name.
    Then ask for their surname and display the length of their surname. Join their first
    name and surname together with a space between and display the result. Finally,
    display the length of their full name (including the space).
    """
    f_name = input("Enter your firstname: ").title()
    print(f"Firstname length: {len(f_name)}")
    l_name = input("Enter your lastname: ").title()
    print(f"Lastname length: {len(l_name)}")
    fullname = " ".join(f_name + l_name)
    return f"Fullname length {len(fullname)} chars."


def display_fav_sub() -> str:
    """
    081
    Ask the user to type in their favourite school subject. Display it
    with “-” after each letter, e.g. S-p-a-n-i-s-h-.
    """
    fav_sub = input("Enter your favorite subject: ")
    [print(s, end="-") for s in fav_sub]
    return ""


def show_poem_extract():
    """
    082
    Show the user a line of text from your favourite poem and ask for a starting and ending point.
    Display the characters between those two points.
    """
    poem = "Se va a hacer, o no se va a hacer, la carnita asada!"
    print(poem)
    start_idx = int(input("Enter a starting index: "))
    end_idx = int(input(f"Enter an ending index up to {len(poem)}: "))
    return poem[start_idx:end_idx]


def force_uppercase():
    """
    083
    Ask the user to type in a word in upper case. If they type it in lower case, ask them to try again.
    Keep repeating this until they type in a message all in uppercase.
    """
    user_input = input("Enter a word in uppercase: ")
    while not user_input.isupper():
        user_input = input("Try again, enter a word in uppercase: ")

    return ""


def uppercase_postcode():
    """
    084
    Ask the user to type in their postcode. Display the first two letters in uppercase.
    """
    postal_code = input("Enter your postal code: ")
    print(postal_code[:2].upper() + postal_code[2:])
    return ""


def num_of_vowels() -> str:
    """
    085
    Ask the user to type in their name and then tell them how many vowels are
    in their name.
    """
    vowels = "aeiou"
    user_name = input("Enter your firstname: ").lower()
    name_vowels = [v for v in user_name if v in vowels]
    return f"There are {len(name_vowels)}vowels in your name."


def save_new_pass() -> str:
    """
    086
    Ask the user to enter a new password. Ask them to enter it again. If the two passwords
    match, display “Thank you”. If the letters are correct but in the wrong case, display the
    message “They must be in the same case”, otherwise display the message “Incorrect”.
    """
    pass1 = input("Enter a new password: ").lower()
    pass2 = input("Retype your new password: ")
    if pass1 == pass2:
        return "Thank you!"
    elif pass1.islower() and not pass2.islower():
        return "They must be in the same case."
    else:
        return "Incorrect!"


def display_reversed_string():
    """
    087
    Ask the user to type in a word and then display it backwards on separate lines. For
    instance, if they type in “Hello” it should display as shown below:
    """
    word = input("Enter a word: ")[::-1]  # Reverse the string
    for char in word:
        print(char)
    return ""


if __name__ == "__main__":
    print(display_reversed_string())
