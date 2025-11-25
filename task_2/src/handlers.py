import turtle
from src.exceptions import ValueIsNotValidException

def parse_rec_depth(input_str: str) -> int:
    if not input_str.isdigit():
        raise ValueIsNotValidException()
    
    int_value = int(input_str)

    if 1 > int_value > 1000:
        raise ValueIsNotValidException()
    
    return int(input_str)

def koch_line(length: float, depth: int):
    if depth == 0:
        turtle.forward(length)
        return
    
    length /= 3
    koch_line(length, depth - 1)
    turtle.left(60)
    koch_line(length, depth - 1)
    turtle.right(120)
    koch_line(length, depth - 1)
    turtle.left(60)
    koch_line(length, depth - 1)


def draw_koch_snowflake(depth: int):
    turtle.speed(0)
    # Move pen up to not trace lines while the cursor is moved
    # left and up from the center
    turtle.penup() 
    # Set a starting position a bit left and up 
    # for the drowing to end in the center
    turtle.goto(-150, 100)
    # Put pen down to start drowing
    turtle.pendown()

    for _ in range(3):
        koch_line(300, depth)
        turtle.right(120)

    # Keeps the window open when the drowing is finished.
    turtle.done()         