from turtle import Turtle, Screen
import random

i = Turtle()
colours = ["Chocolate", "DarkGreen", "SpringGreen", "Magenta",
           "BlueViolet", "IndianRed", "MediumSlateBlue", "Gold"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        i.forward(100)
        i.right(angle)


for sides in range(3, 11):
    i.color(random.choice(colours))
    draw_shape(sides)

screen = Screen()
screen.exitonclick()