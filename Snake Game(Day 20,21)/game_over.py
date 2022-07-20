from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 15, 'normal')


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.write("Game over", move=False, align=ALIGNMENT,
                   font=FONT)
