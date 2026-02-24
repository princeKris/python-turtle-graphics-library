import turtle

def draw_rhombus(side_length=100, angle=60):
    """Draw a rhombus using turtle graphics.
    
    side_length: length of each side
    angle: angle at the top vertex (in degrees)
    """
    screen = turtle.Screen()
    pen = turtle.Turtle()
    pen.speed(5)
    
    # Draw rhombus
    for i in range(4):
        pen.forward(side_length)
        if i % 2 == 0:
            pen.right(180 - angle)
        else:
            pen.right(angle)
    
    pen.hideturtle()
    screen.exitonclick()

if __name__ == "__main__":
    draw_rhombus(100, 60)
