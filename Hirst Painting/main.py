"""Program that simulates a Hirst Dot Painting"""

from turtle import Turtle, Screen
from random import choice

color_list = [(210, 153, 64), (39, 86, 172), (103, 160, 209), (229, 199, 57), (180, 61, 100),
(148, 19, 59), (199, 115, 157), (143, 181, 10), (189, 72, 39), (51, 110, 95),
(65, 53, 42), (12, 66, 135), (57, 52, 67), (187, 78, 103), (60, 50, 64), (96, 107, 170)]

# 10 x 10 rows
# size 20 dots
# separated by 40
screen = Screen()
turtle = Turtle()
turtle.hideturtle()
turtle.speed(0)
screen.colormode(255)
turtle.up()
ROW_NUMBER = 1

turtle.goto(-200, -200)
turtle.speed(6)

def random_color():
    """Picks a random color from the list."""
    turtle.color(choice(color_list))

def row_of_dots(number_of_dots):
    """Sends the turtle forward to draw 10 dots."""
    times_to_repeat = number_of_dots
    random_color()
    turtle.dot(20)
    times_to_repeat -= 1
    if times_to_repeat > 0:
        turtle.forward(40)
        row_of_dots(times_to_repeat)

while ROW_NUMBER <= 10:
    row_of_dots(10)
    if ROW_NUMBER % 2 != 0:
        turtle.seth(90)
        turtle.forward(40)
        turtle.left(90)
    elif ROW_NUMBER % 2 == 0:
        turtle.seth(90)
        turtle.forward(40)
        turtle.right(90)
    ROW_NUMBER +=1

screen.exitonclick()
