"""
118
    Define a subprogram that will ask the user to enter a number and save it as the variable “num”. Define another
    subprogram that will use “num” and count from 1 to that number.
"""


def get_num() -> int:
    num = int(input("Enter a number: "))
    return num


def counter():
    num = get_num()
    for n in range(1, num + 1):
        print(n)
    return ""


if __name__ == "__main__":
    print(counter())
