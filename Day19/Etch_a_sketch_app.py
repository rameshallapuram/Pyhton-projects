from turtle import *

bob = Turtle()


def front():
    bob.forward(20)


def back():
    bob.backward(20)


def up():
    bob.left(10)


def down():
    bob.right(10)


def circle():
    bob.circle(100)


def clear():
    bob.reset()


screen = Screen()
screen.listen()
screen.onkey(front, key="d")
screen.onkey(back, key="a")
screen.onkey(up, key="w")
screen.onkey(down, key="s")
screen.onkey(circle, key="c")
screen.onkey(clear, key="p")

screen.exitonclick()

