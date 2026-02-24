import turtle

t = turtle.Turtle()
t.speed(3)

# Board
for _ in range(2):
    t.forward(220)
    t.left(90)
    t.forward(140)
    t.left(90)

# Stand
t.penup()
t.goto(40, 0)
t.pendown()
t.right(90)
t.forward(50)

t.penup()
t.goto(180, 0)
t.pendown()
t.forward(50)

turtle.done()