import turtle

# L-System rules
def sierpinski_lsystem(iterations, axiom, rules):
    start_string = axiom
    end_string = ""

    for _ in range(iterations):
        end_string = "".join(rules[char] if char in rules else char for char in start_string)
        start_string = end_string

    return end_string

# Draw the L-System
def draw_lsystem(t, instructions, angle, distance):
    for command in instructions:
        if command == 'F':
            t.forward(distance)
        elif command == '+':
            t.right(angle)
        elif command == '-':
            t.left(angle)

# L-System parameters
iterations = 5
axiom = "F-G-G"
rules = {
    "F": "F-G+F+G-F",
    "G": "GG"
}
angle = 120

# Initialize turtle graphics
window = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
t.up()
t.goto(-200, 100)
t.down()

# Generate the L-System string and draw it
instructions = sierpinski_lsystem(iterations, axiom, rules)
draw_lsystem(t, instructions, angle, 10)

# Finish turtle graphics
turtle.done()
