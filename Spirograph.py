import turtle
from turtle import Turtle, Screen
import random
i = Turtle()
turtle.colormode(255)
i.speed("fastest")
turtle.circle(100)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        i.color(random_color())
        i.circle(100)
        i.setheading(i.heading() + size_of_gap)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()