import turtle


def sample1():
    turtle.shape("turtle")
    for node in range(0, 5):
        turtle.forward(100)
        turtle.right(72)
    turtle.exitonclick()


def nested_sample():
    for x in range(0, 10):
        turtle.right(36)
        for y in range(0, 5):
            turtle.forward(100)
            turtle.right(75)

    turtle.exitonclick()


if __name__ == "__main__":
    nested_sample()
