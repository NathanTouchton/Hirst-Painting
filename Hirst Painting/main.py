from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("classic")
timmy.color("purple3")
for _ in range(4):
    timmy.forward(100)
    timmy.right(90)

screen = Screen()
screen.exitonclick()
