import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.bgcolor("white")
screen.title("Three-Phase Power System")

# Create a turtle object
tim = turtle.Turtle()
tim.speed(0)  # Set the fastest speed

# Draw the grid
tim.penup()
tim.goto(-250, -200)
tim.pendown()

for _ in range(5):
    tim.forward(500)
    tim.right(90)
    tim.forward(400)
    tim.right(90)
tim.hideturtle()

# Create a turtle object for sine waves
sine_wave = turtle.Turtle()
sine_wave.speed(0)  # Set the fastest speed

# Set the starting position
sine_wave.penup()
sine_wave.goto(-250, 0)
sine_wave.pendown()

# Draw the three sine waves
colors = ['red', 'green', 'blue']
amplitude = 100
frequency = 1
phase_shifts = [0, math.pi / 3, math.pi * 2 / 3]  # 120-degree phase shifts

for phase, color in zip(phase_shifts, colors):
    sine_wave.color(color)
    sine_wave.penup()
    for x in range(-250, 250, 5):
        y = amplitude * math.sin((x / 50) * frequency + phase)
        sine_wave.goto(x, y)
        sine_wave.pendown()

# Hide the sine wave turtle
sine_wave.hideturtle()

# Keep the window open
screen.mainloop()



