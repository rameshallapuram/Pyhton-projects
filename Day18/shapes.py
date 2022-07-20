import random
from turtle import *

squid = Turtle()
squid.color("Salmon")
squid.shape("turtle")
squid.speed(1)

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        squid.forward(100)
        squid.right(angle)


for shapes in range(3, 11):
    squid.color(random.choice(colours))
    draw_shape(shapes)


screen = Screen()
screen.exitonclick()
