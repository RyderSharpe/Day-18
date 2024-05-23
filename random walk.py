from turtle import *
import random

# Turtle stats
t = Turtle()
t.shape("turtle")
t.color('magenta')
t.pensize(3)
t.shapesize(2, 2, 2)
t.speed(1000)
# Set up the screen
screen = Screen()
screen.setup(width=1000, height=1000)
screen.bgcolor("dodger blue")
screen.title("Shape Project")

color_names = [
    "red", "green", "blue", "purple", "yellow", "orange", "black", "white",
    "gray", "pink", "brown", "cyan", "magenta", "lime", "violet", "teal",
    "navy", "maroon", "olive", "silver", "gold", "coral", "turquoise", "crimson",
    "darkred", "darkgreen", "darkblue", "darkpurple", "darkorange", "darkgray",
    "darkmagenta", "darklime", "darkviolet", "darkcyan", "darkturquoise",
    "fuchsia", "aqua", "salmon", "khaki", "lavender", "beige", "lightblue",
    "lightgreen", "lightyellow", "lightpink", "lightgray", "lightsteelblue",
    "lightcoral", "lightcyan", "lightgoldenrodyellow", "lightseagreen", "lightskyblue"
]

line = 50

numbers = range(1, 101)
random_number = random.choice(numbers)
random_angle = random.randrange(0, 361)

def random_walk(random_number):
    t.color(random.choice(color_names))
    for i in range(random_number):
        t.forward(random_number)
        t.right(random_angle)
for shape_side_n in range(3, 11):
    random_number = random.choice(numbers)  # Generate random number inside the loop
    random_walk(random_number)



screen = Screen()
screen.exitonclick()