import turtle

def gosper_curve(t, order, size, angle=60):
    """ Draw the Gosper Curve using a recursive function. """
    if order == 0:
        t.forward(size)
    else:
        # Expansion rules based on the L-system described
        gosper_a(t, order, size, angle)
        
def gosper_a(t, order, size, angle):
    if order == 0:
        t.forward(size)
    else:
        gosper_a(t, order - 1, size, angle)
        t.left(angle)
        gosper_b(t, order - 1, size, angle)
        t.left(angle)
        t.left(angle)
        gosper_b(t, order - 1, size, angle)
        t.right(angle)
        gosper_a(t, order - 1, size, angle)
        t.right(angle)
        t.right(angle)
        gosper_a(t, order - 1, size, angle)
        gosper_a(t, order - 1, size, angle)
        t.right(angle)
        gosper_b(t, order - 1, size, angle)
        t.left(angle)

def gosper_b(t, order, size, angle):
    if order == 0:
        t.forward(size)
    else:
        t.right(angle)
        gosper_a(t, order - 1, size, angle)
        t.left(angle)
        gosper_b(t, order - 1, size, angle)
        gosper_b(t, order - 1, size, angle)
        t.left(angle)
        t.left(angle)
        gosper_b(t, order - 1, size, angle)
        t.left(angle)
        gosper_a(t, order - 1, size, angle)
        t.right(angle)
        t.right(angle)
        gosper_a(t, order - 1, size, angle)
        t.right(angle)
        gosper_b(t, order - 1, size, angle)

def main():
    window = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)  # Set the turtle's speed to the fastest
    t.penup()
    t.goto(-250, 0)  # Starting position to fit the curve in the screen
    t.pendown()
    
    order = 4  # The depth of recursion, increase for a more complex curve
    size = 10  # Size of each segment, adjust based on recursion depth

    # Start drawing the Gosper Curve
    gosper_curve(t, order, size)
    
    t.hideturtle()

    # Keep the window open until the user closes it manually
    window.mainloop()

if __name__ == "__main__":
    main()
