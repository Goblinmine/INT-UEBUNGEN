import main as api
import turtle
import math

THREASHOLD = 10

# penup if moving distance is higher then THREASHOLD
def goto_threashold(pos: tuple[float, float], turtle: turtle.Turtle) -> None:
    """
    Move a Turtle graphics object to a new position if it is beyond a threshold distance.

    This function calculates the Euclidean distance between the current position of the Turtle
    and the specified position. If the distance is greater than a defined threshold (THRESHOLD),
    the Turtle is lifted (penup), and if not, it is lowered (pendown) and moved to the new position.

    Args:
        pos (tuple[float, float]): A tuple containing the target position (x, y).
        turtle (turtle.Turtle): The Turtle graphics object to be moved.

    Returns:
        None

    Example:
    >>> my_turtle = turtle.Turtle()
    >>> target_position = (50, 50)
    >>> goto_threshold(target_position, my_turtle)
    # The Turtle will be lifted (penup) if the distance to the target is greater than THRESHOLD,
    # or lowered (pendown) and moved to the target position otherwise.
    """
    current_pos = turtle.pos()
    if math.sqrt((pos[0] - current_pos[0])**2 + (pos[1] - current_pos[1])**2) > THREASHOLD: turtle.penup()
    else: turtle.pendown()
    turtle.goto(pos)
    
    
def __write_night(pos: tuple[float, float], text: turtle.Turtle) -> None:
    """
    Display 'Night' or 'Day' on a Turtle graphics screen based on the time at a specific location.

    This function determines whether it is currently nighttime at the specified longitude
    and latitude coordinates using the 'api.is_night' function. It then uses a Turtle graphics
    object to display 'Night' or 'Day' on the screen accordingly.

    Args:
        pos (tuple[float, float]): A tuple containing longitude and latitude.
        turtle (turtle.Turtle): The Turtle graphics object used for text display.

    Returns:
        None

    Example:
    >>> my_turtle = turtle.Turtle()
    >>> target_position = (37.7749, -122.4194)  # San Francisco, CA coordinates
    >>> __write_night(target_position, my_turtle)
    # This function will update the Turtle graphics screen to display 'Night' or 'Day'.
    """
    pos_offset = (pos[0] - 2, pos[1] - 15)
    text.goto(pos_offset)
    is_night = api.is_night(pos)
    text.clear()
    text.write('Night' if is_night else 'Day')
    
    
def iss_loop():
    """
    Continuously update the position of the International Space Station (ISS) on a Turtle graphics screen.

    This function sets up a Turtle graphics screen and displays the current position of the ISS
    by continuously updating the Turtle's position. It also displays 'Night' or 'Day' based on the
    time at the ISS's location.

    Args: None

    Returns:
        None

    Example:
    >>> iss_loop()
    # This function will continuously update the ISS's position and time information on the screen.
    """
    screen = turtle.Screen()
    screen.setup(1000,500)
    screen.bgpic('Jahr 2/api_iss/earth.gif')
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.addshape('Jahr 2/api_iss/iss.gif')
    
    iss = turtle.Turtle()
    iss.shape('Jahr 2/api_iss/iss.gif')
    
    text = turtle.Turtle()
    text.hideturtle()
    text.penup()
    
    while True:
        pos = api.get_iss_position()
        goto_threashold(pos, iss)
        __write_night(pos, text)


def main():
    api.DEBUG = True
    iss_loop()
        

if __name__ == '__main__':
    main()