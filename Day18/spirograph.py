import random
import turtle as t
t.colormode(255)

squid = t.Turtle()
squid.shape("classic")
squid.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(gap_width):
    for _ in range(int(360/gap_width)):
        squid.color(random_color())
        squid.circle(100)
        # current_heading = squid.heading()
        squid.seth(squid.heading() + gap_width)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()