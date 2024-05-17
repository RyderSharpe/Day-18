import turtle
from turtle import *


t = turtle.Turtle()
t.shape("turtle")
t.color('black', 'green')
t.pensize(3)
t.shapesize(2, 2, 2)
t.speed(2)
# Set up the screen (you already created it here)
screen = Screen()
screen.setup(width=1000, height=1000)
screen.bgcolor("dodger blue")
screen.title("This is my first Turtle project. Hurray")


# Draw a cube
for _ in range(2):
    t.color('magenta')
    t.begin_fill()
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.end_fill()
for _ in range(1):
    t.color('SpringGreen')
    t.begin_fill()
    t.left(45)
    t.forward(50)
    t.right(45)
    t.forward(100)
    t.right(135)
    t.forward(50)
    t.end_fill()
for _ in range(1):
    t.color('cyan')
    t.begin_fill()
    t.left(45)
    t.forward(100)
    t.left(135)
    t.forward(50)
    t.left(45)
    t.forward(100)
    t.end_fill()

screen = Screen()
screen.exitonclick()