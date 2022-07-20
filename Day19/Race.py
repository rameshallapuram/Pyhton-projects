import turtle
import random
from turtle import Turtle, Screen

is_race_on = False
turtle.title("Welcome to the turtle race")
screen = Screen()
screen.setup(width=600, height=600)


''' picking color code from colorhexa.com'''
colors = ['purple', 'yellow', 'aqua', 'red', 'orange', 'green', 'brown']
y_position = [-198, -132, -66, 0, 66, 132, 198]
turtle_names = ['bob', 'tim', 'tom', 'jim', 'tesa', 'dash', 'don']

for turtle_index in range(0, 7):
    turtle_names[turtle_index] = Turtle(shape="turtle")
    turtle_names[turtle_index].color(colors[turtle_index])
    turtle_names[turtle_index].penup()
    turtle_names[turtle_index].goto(x=-290, y=y_position[turtle_index])

ref = Turtle()
ref.penup()
ref.goto(x=280, y=-280)
ref.setheading(90)
ref.pendown()
ref.pensize(10)
ref.pencolor("gray")
ref.goto(x=280, y=280)

user_bet = screen.textinput(title="Which color turtle will win?", prompt=f"choose the color from {colors}: ")

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_names:
        if turtle.xcor() >= 270:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You won! The winning turtle is {winning_turtle} turtle.")
            else:
                print(f"You lost! The winner is {winning_turtle} turtle.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
