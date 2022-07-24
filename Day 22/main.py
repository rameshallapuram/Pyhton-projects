import turtle
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time
turtle.penup()

screen = Screen()
screen.screensize(800, 600, "black")
screen.title("Welcome to the Pong Game")
screen.tracer(0)

left_paddle = Paddle()
left_paddle.setposition(-370, 0)

right_paddle = Paddle()
right_paddle.goto(360, 0)

ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(left_paddle.down, "s")
screen.onkeypress(right_paddle.down, "Down")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.01)
    ball.ball_movement()
    # detecting collision with the side walls
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.wall_bounce()
    # detecting collision with the paddle
    if ball.distance(left_paddle) < 30 and ball.xcor() > -370 or ball.distance(right_paddle) < 30 and ball.xcor() < 360:
        ball.paddle_bounce()

    # detecting missing collisions with the paddles
    # right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_score()

    # left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_score()


screen.exitonclick()
