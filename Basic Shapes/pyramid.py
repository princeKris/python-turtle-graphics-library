import turtle

def draw_pyramid(base_size=100, height=100):
    """Draw a 3D pyramid (square base) using turtle graphics."""
    screen = turtle.Screen()
    pen = turtle.Turtle()
    pen.speed(5)
    
    # Draw base square
    pen.penup()
    pen.goto(-base_size/2, 0)
    pen.pendown()
    for _ in range(4):
        pen.forward(base_size)
        pen.right(90)
    
    # Calculate apex position
    apex_x = 0
    apex_y = height
    
    # Draw edges from corners to apex
    corners = [(-base_size/2, 0), (base_size/2, 0), (base_size/2, -base_size/2), (-base_size/2, -base_size/2)]
    for corner in corners:
        pen.penup()
        pen.goto(corner)
        pen.pendown()
        pen.goto(apex_x, apex_y)
    
    # Draw back edges (dashed effect)
    pen.penup()
    pen.goto(base_size/2, -base_size/2)
    pen.pendown()
    pen.goto(-base_size/2, -base_size/2)
    
    pen.hideturtle()
    screen.exitonclick()

if __name__ == "__main__":
    draw_pyramid(100, 100)
