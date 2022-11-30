import turtle

import colorgram
import random
from turtle import Turtle, Screen

colors = colorgram.extract('image.jpg', 30)

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_color = (r, g, b)
    rgb_colors.append(rgb_color)

color_list = [(58, 106, 148), (224, 200, 109), (134, 84, 58), (223, 138, 62), (196, 145, 171), (234, 226, 204),
              (224, 234, 230), (139, 82, 105), (209, 90, 69), (188, 80, 120), (68, 105, 90),
              (237, 225, 233), (134, 182, 136), (133, 133, 74), (63, 156, 92), (48, 156, 194), (183, 192, 201),
              (214, 177, 191), (19, 57, 93), (112, 123, 149), (229, 174, 165), (172, 203, 182),
              (158, 205, 215), (69, 58, 47), (108, 47, 60), (53, 70, 65), (72, 64, 53)]

i = Turtle()
turtle.colormode(255)
i.speed(0)
i.penup()
i.setheading(225)
i.forward(300)
i.setheading(0)
i.hideturtle()

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    i.dot(20, random.choice(color_list))
    i.forward(50)

    if dot_count % 10 == 0:
        i.setheading(90)
        i.forward(50)
        i.setheading(180)
        i.forward(500)
        i.setheading(0)

screen = Screen()
screen.exitonclick()
