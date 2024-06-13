import turtle
import random

# Define the transformations with their probabilities
transformations = [
    (lambda x, y: (0, 0.16 * y), 0.01),  # Stem
    (lambda x, y: (0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6), 0.85),  # Larger leaflets
    (lambda x, y: (0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6), 0.07),  # Left leaflet
    (lambda x, y: (-0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44), 0.07)  # Right leaflet
]

# Initialize the turtle
t = turtle.Turtle()
t.speed(0)
t.penup()
t.setpos(0, -300)
t.pendown()

# Iterate and draw the fern
for _ in range(10000):
    # Choose a random transformation based on probabilities
    rand_num = random.random()
    probability_sum = 0
    chosen_transform = None
    for transform, probability in transformations:
        probability_sum += probability
        if rand_num < probability_sum:
            chosen_transform = transform
            break
    
    # Apply the chosen transformation
    new_x, new_y = chosen_transform(t.xcor(), t.ycor())
    t.goto(new_x, new_y)
    t.dot(1)  # Draw a small dot to represent a leaf

# Hide the turtle and display the final drawing
t.hideturtle()
turtle.done()
