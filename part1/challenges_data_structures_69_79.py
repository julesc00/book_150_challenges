

def show_country():
    """
    069
    Create a tuple containing the names of five countries and display the whole tuple. Ask the user to enter
    one of the countries that have been shown to them and then display the index number (i.e. position in
    the list) of that item in the tuple.
    """
    countries = ("Mexico", "United States", "Russia", "France", "Sweden")
    print(countries)
    user_pick = input("Enter one of the countries from above: ").title()
    if user_pick not in countries:
        return ""
    else:
        return countries.index(user_pick)


def show_country_idx() -> str:
    """
    070
    Add to program 069 to ask the user to enter a number and display the country in that position.
    """
    countries = ("Mexico", "United States", "Russia", "France", "Sweden")
    print(", ".join(countries))
    user_num = int(input(f"Enter a number from 0 to {len(countries)}: "))
    trigger = False
    while not trigger:
        if user_num not in range(0, len(countries)+1):
            user_num = int(input(f"Enter a number from 1 to {len(countries)}: "))
        elif user_num in range(0, len(countries)):
            trigger = True
            return countries[user_num]


def show_favorite_sport():
    """
    071
    Create a list of two sports. Ask the user what their favourite sport is and
    add this to the end of the list. Sort the list and display it.
    """
    sports = ["bodybuilding", "surfing", input("What's your favorite sport?: ")]
    return sorted(sports)


def delete_school_subject():
    """
    072
    Create a list of six school subjects. Ask the user which of these subjects they don’t like. Delete the subject they have chosen from the
    list before you display the list again.
    """
    subjects = ["Physics", "Math", "Biology", "Python Coding", "Databases"]
    trigger = False
    while not trigger:
        print(subjects)
        user_pick = input("Choose a subject you don't like from the above: ").title()
        if user_pick in subjects:
            idx = subjects.index(user_pick)
            del subjects[idx]
            trigger = True
            return subjects


def favorite_foods():
    """
        073
        Ask the user to enter four of their favourite foods and store them in a dictionary so
        that they are indexed with numbers starting from 1. Display the dictionary in full, showing the
        index number and the item. Ask them which they want to get rid of and remove it
        from the list. Sort the remaining data and display the dictionary.
    """
    from collections import OrderedDict
    fav_foods_str = input("Enter 4 favorite foods separated by commas: ")
    fav_foods = fav_foods_str.split(",")
    fav_foods_dict, idx = {idx: f for idx, f in enumerate(fav_foods, start=1)}, 0
    [print(f"{k}. {v}") for k, v in fav_foods_dict.items()]
    user_pick = input("Which food would like to remove: ").lower()
    for k, v in fav_foods_dict.items():
        if user_pick == v:
            idx = k
    fav_foods_dict.pop(idx, "")
    # Sort dict by key, starting index (0)
    o_dict = OrderedDict(sorted(fav_foods_dict.items(), key=lambda i: i[0]))
    return o_dict


def display_colors():
    """
    074
    Enter a list of ten colours. Ask the user for a starting number between 0 and 4
    and an end number between 5 and 9. Display the list for those colours between the start and end
    numbers the user input.
    """
    colors = ["green", "yellow", "pink", "red", "blue", "purple", "orange", "brown", "grey"]
    starting_num = int(input("Enter a starting number from 0 to 4: "))
    ending_num = int(input("Enter an ending number from 5 to 9: "))
    return [color for color in colors[starting_num:ending_num]]


def list_numbers():
    """
    076
    Create a list of four three-digit numbers. Display the list to the user, showing each item from
    the list on a separate line. Ask the user to enter a three-digit number. If the number they
    have typed in matches one in the list, display the position of that number in the list,
    otherwise display the message “That is not in the list”.
    """
    three_digit_lst = [333, 777, 999]
    user_num = int(input("Enter a three-digit number: "))
    return three_digit_lst.index(user_num) if user_num in three_digit_lst else "Not in list"


def show_party_guests():
    """
    076
    Ask the user to enter the names of three people they want to invite to a party and store
    them in a list. After they have entered all three names, ask them if they want to add another. If they do,
    allow them to add more names until they answer “no”. When they answer “no”, display
    how many people they have invited to the party.
    """
    user_count, users, trigger = 3, [], False
    while user_count:
        users.append(input(f"{user_count} users to go; enter a user name: ").title())
        user_count -= 1
    while not trigger:
        ask_user = input("Would you like to add another user? 'y' or 'no': ").lower()
        trigger = True if ask_user == "no" else users.append(input("Add another user: "))

    return f"{len(users)} guests have been invited to your party."


def edit_party_guests_list():
    """
    077
    Change program 076 so that once the user has completed their list of names, display the
    full list and ask them to type in one of the names on the list. Display the position of that
    name in the list. Ask the user if they still want that person to come to the party. If they
    answer “no”, delete that entry from the list and display the list again.
    """
    user_count, users, trigger = 3, [], False
    while user_count:
        users.append(input(f"{user_count} users to go; enter a user name: ").title())
        user_count -= 1
    while not trigger:
        ask_user = input("Would you like to add another user? 'y' or 'no': ").lower()
        trigger = True if ask_user == "no" else users.append(input("Add another user: ").title())

    user_input = input("Enter a guest name to check if he/she has been invited: ").title()
    if user_input not in users:
        return "User not in list"
    else:
        user_answer = input(f"Do you want {user_input} to still come to the party? 'yes' or 'no': ")
        idx = users.index(user_input)
        if user_answer == "no":
            users.remove(users[idx])
    return users


if __name__ == "__main__":
    print(edit_party_guests_list())
