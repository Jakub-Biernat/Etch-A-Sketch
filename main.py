from turtle import Turtle, Screen

my_turtle = Turtle()
my_screen = Screen()
my_screen.listen()


def move_forwards():
    my_turtle.forward(10)


def move_backwards():
    my_turtle.backward(10)


def tilt_counter_clockwise():
    my_turtle.left(10)


def tilt_clockwise():
    my_turtle.right(10)


def clear_screen():
    my_screen.reset()


def etch_a_sketch():
    my_screen.onkey(tilt_counter_clockwise, "a")
    my_screen.onkey(move_forwards, "w")
    my_screen.onkey(tilt_clockwise, "d")
    my_screen.onkey(move_backwards, "s")
    my_screen.onkey(clear_screen, "c")


etch_a_sketch()
my_screen.exitonclick()