from turtle import *
import random
import colorgram

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
# Turtle setup
t = Turtle()
t.shape("turtle")
t.pensize(15)
t.shapesize(2, 2, 2)
t.speed(3)
t.hideturtle()

# Get the screen object
screen = Screen()
screen.setup(width=900, height=900)
screen.bgcolor("dodger blue")
screen.title("Random Dot Project")
# Set color mode using the screen object
screen.colormode(255)

## CHATGPT
# def make_dot():
#     t.dot(20, random.choice(color_list))
#
# # Initial position
# t.penup()
# t.goto(-200, 200)
#
# # Create the 10x10 grid
# for row in range(10):
#     for col in range(10):
#         make_dot()
#         t.forward(50)
#     t.backward(500)
#     t.right(90)
#     t.forward(50)
#     t.left(90)

color_list = [
    (253, 251, 246), (195, 173, 87), (232, 211, 69), (99, 191, 201), (230, 60, 84), (155, 46, 141),
    (115, 110, 176), (215, 237, 224), (243, 169, 186), (167, 219, 241), (165, 195, 45), (18, 137, 206),
    (73, 163, 140), (247, 223, 233), (4, 162, 79), (196, 151, 167), (128, 181, 175), (176, 18, 79),
    (250, 200, 2), (229, 52, 49), (143, 211, 229), (151, 213, 206), (243, 165, 156), (215, 41, 28),
    (35, 160, 209), (211, 16, 14), (187, 182, 210), (120, 5, 103), (243, 13, 22), (81, 44, 123)
]

x = 200
y = 200
def make_dot():
    # Declare as global to modify it inside the function
    global x
    global y
    # starts line of dots
    t.dot(20, random.choice(color_list))
    t.penup()
    t.forward(50)
    t.dot(20, random.choice(color_list))
    y += -5

for i in range(1,11):
    t.penup()
    t.goto(-x, -y)

    # starts line of dots
    for turk in range(1,10):
        make_dot()

screen = Screen()
screen.exitonclick()


# ## CLASS VERSION ##
# import turtle as turtle_module
# import random
#
# turtle_module.colormode(255)
# tim = turtle_module.Turtle()
# tim.speed("fastest")
# tim.penup()
# tim.hideturtle()
# color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# number_of_dots = 100
#
# for dot_count in range(1, number_of_dots + 1):
#     tim.dot(20, random.choice(color_list))
#     tim.forward(50)
#
#     if dot_count % 10 == 0:
#         tim.setheading(90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)
#
#
#
#
#
#
#
#
#
# screen = turtle_module.Screen()
# screen.exitonclick()