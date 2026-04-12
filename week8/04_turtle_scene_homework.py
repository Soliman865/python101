import turtle

# ── YOUR NAME HERE ──
# Name: _______________

turtle.bgcolor("skyblue")   # set the background color

t = turtle.Turtle()
t.speed(5)

# -- Ground --
t.penup()
t.goto(-400, -200)
t.pendown()
t.color("black", "green")
t.begin_fill()
for i in range(2):
    t.forward(800)
    t.right(90)
    t.forward(200)
    t.right(90)
t.end_fill()

# -- House body --
t.penup()
t.goto(-20, -100)
t.pendown()
t.color("black", "white")
t.begin_fill()
for i in range(4):
    t.forward(120)
    t.right(90)
t.end_fill()

# -- Roof --
t.penup()
t.goto(-40, -100)
t.pendown()
t.color("black", "red")
t.begin_fill()
for i in range(3):
    t.forward(160)
    t.left(120)
t.end_fill()


# -- House body --
t.penup()
t.goto(-200, -90)
t.pendown()
t.color("black", "white")
t.begin_fill()
for i in range(4):
    t.forward(120)
    t.right(90)
t.end_fill()

# -- Roof --
t.penup()
t.goto(-220, -90)
t.pendown()
t.color("black", "red")
t.begin_fill()
for i in range(3):
    t.forward(160)
    t.left(120)
t.end_fill()

# -- Sun (circle) --
t.penup()
t.goto(180, 80)
t.pendown()
t.color("black", "yellow")
t.begin_fill()
t.circle(40)
t.end_fill()

t.hideturtle()
turtle.done()

