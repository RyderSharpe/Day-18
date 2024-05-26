from turtle import *
import random

# Turtle stats
t = Turtle()
t.shape("turtle")
#t.color('magenta')
t.pensize(15)
t.shapesize(2, 2, 2)
t.speed(5)


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

line = 50

# Generate turning angles (from, to, in-steps-of)
turn = []
for i in range(0, 361, 45):
    turn.append(i)

## CLASS ##
for _ in range(200):
    t.color(random_colour())
   # t.color(random.choice(random_colour()))
    t.forward(30)
    t.setheading(random.choice(turn))

screen = Screen()
screen.exitonclick()


# def random_walk(random_number):
#     for i in range(random_number):
#         t.color(random.choice(color_names))
#         t.forward(random.choice(line))
#         random_turn = random.choice(turn)
#         t.setheading(random_turn)
#
# for walk in range(1, 110):
#     random_walk(walk)
