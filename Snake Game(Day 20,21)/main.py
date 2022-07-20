import turtle
from turtle import Turtle, Screen
import time
from snake import Snake
from food import *
from score_board import *
from game_over import *
turtle.speed("fastest")
screen = Screen()
screen.screensize(500, 500, "black")
screen.title("My Snake Game")

snake = Snake()

food = Food()
score_board = ScoreBoard()


screen.listen()
# setting control keys for the game
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # Detecting collision of food.
    if snake.snake_head.distance(food) < 10:
        food.refresh()
        snake.extend()
        score_board.update_score()

    # Detecting collision with wall.
    if snake.snake_head.xcor() > 300 or snake.snake_head.xcor() < -300 or snake.snake_head.ycor() > 300 or \
            snake.snake_head.ycor() < -300:
        game_on = False
        GameOver()

    # Detecting the collision with the snake body.
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            GameOver()


screen.exitonclick()
