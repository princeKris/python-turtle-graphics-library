import turtle
import math

def draw_tetrahedron(size=100):
    """Draw a 3D tetrahedron (triangular pyramid) using turtle graphics."""
    screen = turtle.Screen()
    pen = turtle.Turtle()
    pen.speed(5)
    
    # Base triangle vertices
    height_base = size * math.sqrt(3) / 2
    v1 = (-size/2, 0)
    v2 = (size/2, 0)
    v3 = (0, height_base)
    
    # Apex (top vertex)
    apex = (0, height_base * 0.8)
    
    # Draw base triangle
    pen.penup()
    pen.goto(v1)
    pen.pendown()
    pen.goto(v2)
    pen.goto(v3)
    pen.goto(v1)
    
    # Draw edges from base vertices to apex
    pen.penup()
    pen.goto(v1)
    pen.pendown()
    pen.goto(apex)
    
    pen.penup()
    pen.goto(v2)
    pen.pendown()
    pen.goto(apex)
    
    pen.penup()
    pen.goto(v3)
    pen.pendown()
    pen.goto(apex)
    
    pen.hideturtle()
    screen.exitonclick()

if __name__ == "__main__":
    draw_tetrahedron(100)
