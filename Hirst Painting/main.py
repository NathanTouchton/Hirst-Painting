from turtle import Turtle, Screen
from random import randint

turtle = Turtle()
turtle.shape("classic")
# turtle.color("purple3")
shape_sides = 3
screen = Screen()
screen.colormode(255)

for _ in range(8):
    turtle.color(randint(0, 255),
          randint(0, 255),
          randint(0, 255))
    degrees = 360 / shape_sides
    times_to_repeat = shape_sides
    while times_to_repeat > 0:
        turtle.forward(100)
        turtle.right(degrees)
        times_to_repeat -= 1
    shape_sides += 1


screen.exitonclick()
