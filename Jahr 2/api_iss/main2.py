import main as api
import turtle
import math

THREASHOLD = 10

def setup_turtles():
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
    
    return screen, iss, text

# penup if moving distance is higher then THREASHOLD
def goto_threashold(pos: tuple[float, float], turtle: turtle.Turtle) -> None:
    current_pos = turtle.pos()
    if math.sqrt((pos[0] - current_pos[0])**2 + (pos[1] - current_pos[1])**2) > THREASHOLD: turtle.penup()
    else: turtle.pendown()
    turtle.goto(pos)
    
    
def write_night(pos: tuple[float, float], turtle: turtle.Turtle) -> None:
    pos_offset = (pos[0] - 2, pos[1] - 15)
    turtle.goto(pos_offset)
    is_night = api.is_night(pos)
    turtle.clear()
    turtle.write('Night' if is_night else 'Day')


def main():
    screen, iss, text = setup_turtles()
    pos: tuple[float, float]
    while True:
        pos = api.get_iss_position()
        goto_threashold(pos, iss)
        write_night(pos, text)

if __name__ == '__main__':
    main()