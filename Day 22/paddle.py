from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(1, 3, 1)
        self.seth(90)

    def up(self):
        self.seth(90)
        self.forward(50)

    def down(self):
        self.seth(270)
        self.forward(50)




