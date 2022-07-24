from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_point = 0
        self.right_point = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-50, 170)
        self.write(self.left_point, align="center", font=("Courier", 80, "normal"))
        self.goto(50, 170)
        self.write(self.right_point, align="center", font=("Courier", 80, "normal"))

    def left_score(self):
        self.left_point += 1
        self.update_scoreboard()

    def right_score(self):
        self.right_point += 1
        self.update_scoreboard()

