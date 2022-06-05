from turtle import Turtle, Screen
from random import randint, choice

turtle = Turtle()
turtle.shape("classic")
shape_sides = 3
screen = Screen()
screen.colormode(255)
turtle.pensize(10)
turtle.speed(6)

HEADINGS = [0, 90, 180, 270]

for _ in range(50):
    turtle.color(randint(0, 255),
          randint(0, 255),
          randint(0, 255))
    turtle.seth(choice(HEADINGS))
    turtle.forward(100)

screen.exitonclick()
