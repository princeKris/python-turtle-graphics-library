import turtle
import math

def draw_ellipse(semi_major_axis=100, semi_minor_axis=60):
    """Draw an ellipse using turtle graphics.
    
    semi_major_axis: half the length of the major (longer) axis
    semi_minor_axis: half the length of the minor (shorter) axis
    """
    screen = turtle.Screen()
    pen = turtle.Turtle()
    pen.speed(0)
    
    pen.penup()
    pen.goto(semi_major_axis, 0)
    pen.pendown()
    
    # Draw ellipse using parametric equations
    for angle in range(361):
        x = semi_major_axis * math.cos(math.radians(angle))
        y = semi_minor_axis * math.sin(math.radians(angle))
        pen.goto(x, y)
    
    pen.hideturtle()
    screen.exitonclick()

if __name__ == "__main__":
    draw_ellipse(100, 60)
