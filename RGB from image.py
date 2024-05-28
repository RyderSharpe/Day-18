import colorgram
from turtle import *
import random
### READ THIS RYDER ###

# # colorgram.extract returns Color objects, which let you access
# # RGB, HSL, and what proportion of the image was that color.
# first_color = colors[0]
# rgb = first_color.rgb # e.g. (255, 151, 210)
# hsl = first_color.hsl # e.g. (230, 255, 203)
# proportion  = first_color.proportion # e.g. 0.34
#
# # RGB and HSL are named tuples, so values can be accessed as properties.
# # These all work just as well:
# red = rgb[0]
# red = rgb.r
# saturation = hsl[1]
# saturation = hsl.s
###

# # Extract colors from an image.
# rgb_colors = []
# colors = colorgram.extract('hirst.jpg', 60)
# for color in colors:
#     # rgb_colors.append(color.rgb)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

# TODO- 10x10 dots. 20 in size. Spaced apart by 50 paces

# Turtle stats
t = Turtle()
t.shape("turtle")
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

color_list = [
    (253, 251, 246), (195, 173, 87), (232, 211, 69), (99, 191, 201), (230, 60, 84), (155, 46, 141),
    (115, 110, 176), (215, 237, 224), (243, 169, 186), (167, 219, 241), (165, 195, 45), (18, 137, 206),
    (73, 163, 140), (247, 223, 233), (4, 162, 79), (196, 151, 167), (128, 181, 175), (176, 18, 79),
    (250, 200, 2), (229, 52, 49), (143, 211, 229), (151, 213, 206), (243, 165, 156), (215, 41, 28),
    (35, 160, 209), (211, 16, 14), (187, 182, 210), (120, 5, 103), (243, 13, 22), (81, 44, 123)
]

x = 400
y = 400
def make_dot():
    global x  # Declare as global to modify it inside the function
    global y
    # starts line of dots
    for turk in range(1):
        t.dot(20, random.choice(color_list))
        t.penup()
        t.forward(50)
        t.dot(20, random.choice(color_list))
        y += -5

for i in range(1,11):
    t.penup()
    t.goto(-x, -y)

    # starts line of dots
    for turk in range(1,11):
        make_dot()





    # for turt in range(1,11):
    #     j += -50
    #     t.penup()
    #     t.goto(-j, -j)
    #     t.dot(20, random.choice(color_list))
    #     t.penup()
    #     t.forward(50)
    #     t.pendown()





screen = Screen()
screen.exitonclick()