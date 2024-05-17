import turtle
import random

# Create the turtle and screen objects
t = turtle.Turtle()
t.shape("turtle")
t.pensize(3)
t.speed(30)

screen = turtle.Screen()
screen.setup(width=1000, height=800)
screen.bgcolor("dodger blue")
screen.title("This is my first Turtle project. Hurray")
screen.colormode(255)
def random_colour():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  return (r, g, b)

# Draw shapes with loop and adjust angle for each shape
for sides in range(3, 11):  # Loop from 3 to 10 sides (triangle to decagon)
  t.color(random_colour())
  for _ in range(sides):
    t.forward(100)
    t.right(360 / sides)  # Calculate angle based on number of sides

# Call exitonclick only once at the end
screen.exitonclick()