
def get_data():
    user_name = input("Enter your name: ").title()
    user_age = int(input("Enter your age in numbers: "))
    data_tuple = (user_name, user_age)
    return data_tuple


def message(name: str, age: int) -> str:
    if age <= 10:
        print("Hi ", name)
    else:
        print("hello ", name)

    return f"{name}, you are {age} years old!"


if __name__ == "__main__":
    user_data = get_data()
    print(message(user_data[0], user_data[1]))
