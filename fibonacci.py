# Draw the Fibonacci Spiral using Turtle Graphics

from turtle import *
from turtle import Turtle, Screen
fibo_nr = [1, 1, 2, 3, 5, 8, 13, 21, 34]  # Fibonacci numbers this could be calculated instead
screen = Screen()
screen.setup(width=600, height=400)
screen.bgcolor("dodger blue")
screen.title("Fibonacci")

def draw_square(side_length):  # Function for drawing a square
    for i in range(4):
        forward(side_length)
        right(90)


nr_squares = len(fibo_nr)

factor = 3  # Enlargement factor
penup()
goto(50, 50)  # Move starting point right and up
pendown()
for i in range(nr_squares):
    draw_square(factor * fibo_nr[i])  # Draw square
    penup()  # Move to new corner as starting point
    forward(factor * fibo_nr[i])
    right(90)
    forward(factor * fibo_nr[i])
    pendown()

penup()
goto(50, 50)  # Move to starting point
setheading(0)  # Face the turtle to the right
pencolor('red')
pensize(3)
pendown()

# Draw quartercircles with fibonacci numbers as radius
for i in range(nr_squares):
    circle(-factor * fibo_nr[i], 90)  # minus sign to draw clockwise


screen = Screen()
screen.exitonclick()

