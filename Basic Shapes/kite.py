import turtle

def draw_kite(top_length=80, bottom_length=60, left_width=50, right_width=50):
    """Draw a kite shape using turtle graphics.
    
    A kite has two pairs of adjacent equal sides.
    """
    screen = turtle.Screen()
    pen = turtle.Turtle()
    pen.speed(5)
    
    # Start at top vertex
    pen.penup()
    pen.goto(0, top_length)
    pen.pendown()
    
    # Draw to right vertex
    pen.goto(right_width, 0)
    
    # Draw to bottom vertex
    pen.goto(0, -bottom_length)
    
    # Draw to left vertex
    pen.goto(-left_width, 0)
    
    # Return to top vertex
    pen.goto(0, top_length)
    
    # Draw diagonal symmetry lines
    pen.penup()
    pen.goto(0, top_length)
    pen.pendown()
    pen.goto(0, -bottom_length)
    
    pen.penup()
    pen.goto(-left_width, 0)
    pen.pendown()
    pen.goto(right_width, 0)
    
    pen.hideturtle()
    screen.exitonclick()

if __name__ == "__main__":
    draw_kite(80, 60, 50, 50)
