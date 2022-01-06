import math


def multiply_by_two():
    """
    027
    Ask the user to enter a number with lots of decimal places. Multiply
    this number by two and display the answer.
    """
    num = int(input("Enter an number: "))
    return num * 2


def multiply_by_two_decimals() -> float:
    """
    028
    Update program 027 so that it will display the answer to two decimal places.
    """
    decimal_num = float(multiply_by_two())
    return decimal_num


def square_num():
    """
    029
    Ask the user to enter an integer that is over 500. Work out the square
    root of that number and display it to two decimal places.
    """
    trigger = False
    while not trigger:
        num = int(input("Enter a number above 500: "))
        if num > 500:
            trigger = True
            return round(math.sqrt(num), 2)


def pi_five_decimals():
    """
    030
    Display pi (π) to five decimal places.
    """
    return round(math.pi, 5)


def find_circle_radius():
    """
    031
    Ask the user to enter the radius of a circle (measurement from the
    centre point to the edge). Work out the area of the circle (π*radius2).
    """
    radius = float(input("Enter the radius of a circle: "))
    circle_area = round(math.pi * (radius ** 2), 4)
    return circle_area


def radius_x_depth():
    """
    032
    Ask for the radius and the depth of a cylinder and work out the total
    volume (circle area*depth) rounded to three decimal places.
    """
    radius = float(input("Enter the cirle area: "))
    depth = float(input("Enter the depth of cylinder: "))
    circle_area = math.pi * (radius ** 2)
    total_volume = round(circle_area * depth, 3)
    return total_volume


def divide_and_remainder():
    """
    033
    Ask the user to enter two numbers. Use whole number division to divide
    the first number by the second and also work out the remainder and display
    the answer in a user-friendly way (e.g. if they enter 7 and 2 display
    “7 divided by 2 is 3 with 1 remaining”).
    """
    num1 = int(input("Enter any number: "))
    num2 = int(input("Enter another number: "))
    try:
        result = num1 // num2
        remainder = num1 % num2
        return f"{num1} divided by {num2} is {result} with remainder {remainder}."
    except ZeroDivisionError:
        return "You cannot divide by zero"


def shape_dimensions():
    """
    034
    Ask the user to enter two numbers. Use whole number division to divide
    the first number by the second and also work out the remainder and
    display the answer in a user-friendly way (e.g. if they enter 7 and 2
    display “7 divided by 2 is 3 with 1 remaining”).
    """
    shape = int(input("Select a shape: \n\t1) Square\n\t2) Triangle "))
    if shape == 1:
        sqr_length = int(input("Enter the length of 1 side: "))
        sqr_area = sqr_length * sqr_length
        return f"The square area is {sqr_area}"
    elif shape == 2:
        tri_base = int(input("Enter the triangle's base: "))
        tri_height = int(input("Enter the triangle's height: "))

        return f"The triangle area is {(tri_base * tri_height) / 2}"
    else:
        return "Incorrect option selected."


if __name__ == "__main__":
    print(divide_and_remainder())
