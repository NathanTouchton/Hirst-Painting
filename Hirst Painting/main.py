"""Program that simulates a Hirst Dot Painting"""

from turtle import Turtle, Screen
from random import choice

color_list = [(210, 153, 64), (39, 86, 172), (103, 160, 209), (229, 199, 57), (180, 61, 100),
(148, 19, 59), (199, 115, 157), (143, 181, 10), (189, 72, 39), (51, 110, 95),
(65, 53, 42), (12, 66, 135), (57, 52, 67), (187, 78, 103), (60, 50, 64), (96, 107, 170)]

# 10 x 10 rows
# size 20 dots
# separated by 20
screen = Screen()
turle = Turtle()
turle.hideturtle()
turle.speed(3)
turle.pensize(20)
screen.colormode(255)

def random_color():
    """Picks a random color from the list."""
    turle.color(choice(color_list))

screen.exitonclick()
