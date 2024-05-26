from turtle import *
import random

# Turtle stats
turtle = Turtle()
turtle.shape("turtle")
turtle.pensize(3)
turtle.shapesize(2, 2, 2)
turtle.speed(500)

# Get the screen object
screen = Screen()
screen.setup(width=1000, height=1000)
screen.bgcolor("dodger blue")
screen.title("Shape Project")
# Set color mode using the screen object
screen.colormode(255)

def random_colour():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  random_colour = (r, g, b)
  return random_colour


# ## RYDERS ##
# circle = 361
# j = 0
# for _ in range(0, circle):
#     turtle.color(random_colour())
#     turtle.circle(100)
#     turtle.setheading(j)
#     j += 1


# CLASS ##
########## Challenge 5 - Spirograph ########

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        turtle.color(random_colour())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + size_of_gap)

draw_spirograph(5)


screen = Screen()
screen.exitonclick()