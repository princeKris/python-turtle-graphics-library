import turtle
import math

def draw_cone(radius=50, height=100):
    """Draw a 3D cone using turtle graphics."""
    screen = turtle.Screen()
    pen = turtle.Turtle()
    pen.speed(7)
    
    # Draw base ellipse
    pen.penup()
    pen.goto(-radius, 0)
    pen.pendown()
    for angle in range(361):
        x = radius * math.cos(math.radians(angle))
        y = (radius * 0.3) * math.sin(math.radians(angle))
        pen.goto(x, y)
    
    # Draw left side from base to apex
    pen.penup()
    pen.goto(-radius, 0)
    pen.pendown()
    pen.goto(0, height)
    
    # Draw right side from base to apex
    pen.penup()
    pen.goto(radius, 0)
    pen.pendown()
    pen.goto(0, height)
    
    # Draw hidden base line
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.setheading(0)
    pen.forward(radius)
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.setheading(180)
    pen.forward(radius)
    
    pen.hideturtle()
    screen.exitonclick()

if __name__ == "__main__":
    draw_cone(50, 100)
