import turtle
from turtle import *

t = turtle.Turtle()
t.shape("turtle")
t.color('black', 'green')
t.pensize(3)
t.shapesize(2, 2, 2)
t.speed(3)
# Set up the screen (you already created it here)
screen = Screen()
screen.setup(width=1000, height=800)
screen.bgcolor("dodger blue")
screen.title("This is my first Turtle project. Hurray")


# Draw a cube
for _ in range(10):
    t.color('snow')
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()


screen = Screen()
screen.exitonclick()