import random
import turtle

import colorgram as cl
from turtle import Turtle, Screen
colors = cl.extract('colors_spots.jpg', 30)


rgb_colors = []


def list_colors():
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)
        return rgb_colors


colors_list = [(215, 166, 17), (205, 153, 99),(225, 205, 103), (161, 55, 101), (113, 187, 213), (154, 31, 58),
               (8, 109, 166), (42, 13, 24),(160, 29, 25), (12, 23, 52), (34, 122, 62), (59, 23, 18), (9, 32, 26),
               (186, 156, 173), (63, 166, 88), (171, 57, 42), (156, 208, 215), (94, 183, 167), (205, 99, 95),
               (240, 200, 3), (213, 174, 198),(28, 37, 105), (187, 99, 110), (163, 209, 197), (220, 177, 173),
               (14, 105, 56)]

screen = Screen()
screen.title("Welcome to the hirst Painting")
screen.screensize(600, 600)

turtle.colormode(255)
bob = Turtle()
bob.shape("turtle")
bob.speed("fastest")
bob.penup()
bob.goto(-300, -300)

number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    bob.dot(20, random.choice(colors_list))
    bob.forward(50)
    if dot_count == 100:
        bob.hideturtle()

    if dot_count % 10 == 0:
        bob.setheading(90)
        bob.forward(50)
        bob.setheading(180)
        bob.forward(500)
        bob.setheading(0)











screen.exitonclick()

