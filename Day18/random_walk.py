"""creating a program to generate random patterns"""
import random
from turtle import *

squid = Turtle()
squid.color("Salmon")
squid.shape("turtle")
squid.speed(6)
squid.pensize(6)

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
           "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

directions = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330]

for _ in range(200):
    squid.pencolor(random.choice(colours))
    squid.seth(random.choice(directions))
    squid.forward(30)
