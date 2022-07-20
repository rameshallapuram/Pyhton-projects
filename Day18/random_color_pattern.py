import random
import turtle as t
t.colormode(255)

squid = t.Turtle()
squid.shape("turtle")
squid.speed(6)
squid.pensize(6)


def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    color = (r, g, b)
    return color


directions = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330]

for _ in range(200):
    squid.pencolor(random_color())
    squid.seth(random.choice(directions))
    squid.forward(30)
