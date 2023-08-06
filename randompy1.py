import turtle
import random

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle object
pen = turtle.Turtle()
pen.speed(0)  # Fastest drawing speed

# Set initial size and angle values
size = 1
angle = 170

# Define a function to generate a random RGB color
def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

def draw_pattern(size):  # Pass 'size' as an argument
    for _ in range(300):
        pen.color(random_color())
        pen.forward(size)
        pen.left(angle)
        size += 1  # Increase the size for a bigger pattern

# Call the draw_pattern function with the initial 'size' value
draw_pattern(size)
turtle.Screen().mainloop()
