from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.shape("circle")
tim.shapesize(.1)


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def counter_clock():
    tim.left(10)


def clock():
    tim.right(10)


def clear():
    tim.clear()
    tim.reset()
    tim.shapesize(.1)


screen.listen()
screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=counter_clock, key="a")
screen.onkey(fun=clock, key="d")
screen.onkey(fun=clear, key="c")
screen.exitonclick()
