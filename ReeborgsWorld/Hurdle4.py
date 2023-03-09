# Jonas Millonig
# 08. 03. 2023
# Reeborg's Wrold | Hurdle 4

def nextStep():
    if right_is_clear():
        turn_right()
    elif left_is_clear():
        turn_left()
    elif not front_is_clear():
        turn_arround()
    move()
    
def turn_right():
    for i in range (3):
        turn_left()
        
def left_is_clear():
    output = False
    turn_arround()
    output = right_is_clear()
    turn_arround()
    return output

def turn_arround():
    for i in range(2):
        turn_left()

while not at_goal():
    nextStep()