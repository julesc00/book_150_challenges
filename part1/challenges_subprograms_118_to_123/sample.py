
def get_name():
    user_name = input("Enter your name: ").title()
    return user_name


def print_msg(name: str) -> str:
    return f"Hello {name}"


if __name__ == "__main__":
    user_name = get_name()
    print(user_name)
