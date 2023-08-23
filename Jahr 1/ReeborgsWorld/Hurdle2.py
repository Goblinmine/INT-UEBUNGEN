# Jonas Millonig
# 08. 03. 2023
# Reeborg's Wrold | Hurdle 2

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
                  
                  
def turn_right():
    for i in range(3):
        turn_left()


while not at_goal():
    if wall_in_front():
        jump()
    move()