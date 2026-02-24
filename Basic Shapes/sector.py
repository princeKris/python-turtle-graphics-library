import turtle
import math

def draw_sector(radius=80, angle=90):
    """Draw a sector (pie slice) of a circle using turtle graphics.
    
    radius: radius of the circle
    angle: central angle of the sector (in degrees)
    """
    screen = turtle.Screen()
    pen = turtle.Turtle()
    pen.speed(0)
    
    # Draw two radii
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.goto(radius, 0)
    
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.setheading(angle)
    pen.forward(radius)
    
    # Draw arc
    pen.penup()
    pen.goto(radius, 0)
    pen.pendown()
    
    # Calculate arc steps
    steps = int(angle) + 1
    for i in range(steps):
        current_angle = (i / steps) * angle
        x = radius * math.cos(math.radians(current_angle))
        y = radius * math.sin(math.radians(current_angle))
        pen.goto(x, y)
    
    pen.hideturtle()
    screen.exitonclick()

if __name__ == "__main__":
    draw_sector(80, 90)
