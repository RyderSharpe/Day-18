import turtle
import random

# Create the turtle and screen objects
t = turtle.Turtle()
t.shape("turtle")
t.pensize(3)
t.speed(1000)

# Get the screen object
screen = turtle.Screen()
screen.setup(width=1000, height=1000)
screen.bgcolor("dodger blue")
screen.title("This is my first Turtle project. Hurray")

# Set color mode using the screen object
screen.colormode(255)

def random_colour():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  return (r, g, b)

j = 10
for _ in range(200):
  t.color(random_colour())
  j += 1
  t.left(45)
  t.forward(j)
  t.right(1)
  t.forward(j)
  t.left(45)

# Call exitonclick only once at the end
screen.exitonclick()
