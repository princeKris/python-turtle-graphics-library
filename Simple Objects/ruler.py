import turtle

t = turtle.Turtle()
t.speed(3)

# Ruler base
for _ in range(2):
    t.forward(250)
    t.left(90)
    t.forward(30)
    t.left(90)

# Marks
t.penup()
t.goto(0, 0)
t.pendown()
for i in range(0, 250, 20):
    t.penup()
    t.goto(i, 30)
    t.pendown()
    t.right(90)
    t.forward(10)
    t.left(90)

turtle.done()