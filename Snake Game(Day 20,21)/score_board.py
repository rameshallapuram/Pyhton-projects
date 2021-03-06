from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0   # keeping track of the score
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 290)
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT,
                   font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT,
                   font=FONT)

















