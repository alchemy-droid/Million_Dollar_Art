import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
i = Turtle()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

directions = [0, 90, 180, 270]

is_draw = True
while is_draw:
    i.color(random_color())
    i.pensize(15)
    i.speed(0)
    i.forward(20)
    i.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()