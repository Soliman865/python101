import turtle

# --- Ask the user for input ---
sides = int(input("How many sides? (3 = triangle, 4 = square, 5 = pentagon...): "))
size  = int(input("How long should each side be? (try 50 to 200): "))
color = input("What outline color? (red, blue, green, purple, orange...): ")
fill  = input("What fill color? (yellow, pink, cyan, .....): ")

# --- Calculate the turning angle ---
angle = 360 / sides   # the 360° rule

# --- Draw the shape ---
t = turtle.Turtle()
t.speed(5)
t.color(color)        # outline color
t.fillcolor(fill)     

t.begin_fill()

for i in range(sides):
    t.forward(size)
    t.right(angle)

t.end_fill()
t.hideturtle()
turtle.done() a string
# - angle = 360 / sides is the key formula — emphasize this
# - Students who finish early should attempt Challenge B or C
