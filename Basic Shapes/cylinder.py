import turtle
import math

def draw_cylinder(radius=50, height=100):
    """Draw a 3D cylinder using turtle graphics."""
    screen = turtle.Screen()
    pen = turtle.Turtle()
    pen.speed(7)
    
    # Draw top ellipse
    pen.penup()
    pen.goto(-radius, height)
    pen.pendown()
    for angle in range(361):
        x = radius * math.cos(math.radians(angle))
        y = height + (radius * 0.3) * math.sin(math.radians(angle))
        pen.goto(x, y)
    
    # Draw left side
    pen.penup()
    pen.goto(-radius, height)
    pen.pendown()
    pen.goto(-radius, 0)
    
    # Draw right side
    pen.penup()
    pen.goto(radius, height)
    pen.pendown()
    pen.goto(radius, 0)
    
    # Draw bottom ellipse
    pen.penup()
    pen.goto(-radius, 0)
    pen.pendown()
    for angle in range(361):
        x = radius * math.cos(math.radians(angle))
        y = (radius * 0.3) * math.sin(math.radians(angle))
        pen.goto(x, y)
    
    pen.hideturtle()
    screen.exitonclick()

if __name__ == "__main__":
    draw_cylinder(50, 100)
