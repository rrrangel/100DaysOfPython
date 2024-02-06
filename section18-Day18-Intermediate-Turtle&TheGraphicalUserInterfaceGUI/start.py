from turtle import Turtle, Screen
import turtle as t
import random
import heroes

print(heroes.gen())

# colors = ["IndianRed", "SeaGreen", "DarkOrchid", "orange", "CornflowerBlue", "SlateGray", "DeepSkyBlue"]
directions = [0, 90, 180, 270]

tim = Turtle()
t.colormode(255)
tim.shape("turtle")
tim.color("red", "green")
# tim.pensize(15)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_clr = (r, g, b)
    return random_clr


# Draw a square
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)


# Draw dashed lines
# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# Draw Shape (Num Sides)
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors), "green")
#     draw_shape(shape_side_n)

# Random Walk
# for _ in range(200):
#     tim.color(random_color(), "green")
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# Spirograph
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color(), "green")
        tim.circle(100)
        tim.setheading(tim.heading() + 10)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()
