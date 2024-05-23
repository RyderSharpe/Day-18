from turtle import *
import random

t = Turtle()
t.shape("turtle")
t.color('magenta')
t.pensize(3)
t.shapesize(2, 2, 2)
t.speed(1000)
# Set up the screen (you already created it here)
screen = Screen()
screen.setup(width=1000, height=1000)
screen.bgcolor("dodger blue")
screen.title("Shape Project")

color_names = [
    "red", "green", "blue", "purple", "yellow", "orange", "black", "white",
    "gray", "pink", "brown", "cyan", "magenta", "lime", "violet", "teal",
    "navy", "maroon", "olive", "silver", "gold", "coral", "turquoise", "crimson",
    "darkred", "darkgreen", "darkblue", "darkpurple", "darkorange", "darkgray",
    "darkmagenta", "darklime", "darkviolet", "darkteal", "darkcyan", "darkturquoise",
    "fuchsia", "aqua", "salmon", "khaki", "lavender", "beige", "lightblue",
    "lightgreen", "lightyellow", "lightpink", "lightgray", "lightsteelblue",
    "lightcoral", "lightcyan", "lightgoldenrodyellow", "lightseagreen", "lightskyblue"
]
line = 100

# ## MY VERSION ##
# for iteration in range(3,9):
#     #t.color(random.choice(color_list))
#     for shape in range(iteration):
#         t.forward(line)
#         t.right(360 / iteration)


## CLASS VERSION 33
def draw_shape(num_sides):
    angle = 360 / num_sides
    t.color(random.choice(color_names))
    for i in range(num_sides):
        t.forward(line)
        t.right(angle)
for shape_side_n in range(3,110):
    draw_shape(shape_side_n)

## JUST FUN ##
#     for shape in range(iteration):
#         t.color('red')
#         t.forward(line)
#         t.left(360 / iteration)
#
#
# t.left(180)
# for iteration in range(3,15):
#     for shape in range(iteration):
#         t.color('cyan')
#         t.forward(line)
#         t.right(360 / iteration)
# for iteration in range(3,15):
#     for shape in range(iteration):
#         t.color('white')
#         t.forward(line)
#         t.left(360 / iteration)
#
#
# t.left(180)
# t.forward(100)
# for iteration in range(3,15):
#     for shape in range(iteration):
#         t.color('cyan')
#         t.forward(line)
#         t.right(360 / iteration)
# for iteration in range(3,15):
#     for shape in range(iteration):
#         t.color('white')
#         t.forward(line)
#         t.left(360 / iteration)



screen = Screen()
screen.exitonclick()
