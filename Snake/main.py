from snake import Snake
from turtle import Turtle, Screen
import turtle
import time
import asyncio
import random

food = []


snake = Snake(food, 3)

grid_unit = 20
size = 30


SIZEX = grid_unit*size
SIZEY = grid_unit*size

Screen().setup(SIZEX+3*grid_unit, SIZEY+3*grid_unit)
Screen().colormode(255)


# region draw board
board_turtle = Turtle(visible=False)
board_turtle.penup()
board_turtle.speed(0)
board_turtle.pensize(grid_unit-3)

board_turtle.goto(-SIZEX/2-grid_unit, -SIZEY/2-grid_unit)
board_turtle.pendown()
board_turtle.setheading(0)
for _ in range(4):
    board_turtle.forward(SIZEX+2*grid_unit)
    board_turtle.left(90)  
# endregion

# debug
# board_turtle.color(200, 200, 200)
# board_turtle.goto(SIZEX/2, SIZEX/2)
# board_turtle.goto(SIZEX/2, -SIZEX/2)
# board_turtle.goto(-SIZEX/2, SIZEX/2)
# board_turtle.goto(-SIZEX/2, -SIZEX/2)

# region food
food_turtle = Turtle(visible=False)
food_turtle.penup()
food_turtle.speed(0)

def add_food(how_many, food: list[tuple[int, int]]):
    if len(food) < how_many:
        new_food = (
            random.randint(-(size/2), size/2)*grid_unit,
            random.randint(-(size/2), size/2)*grid_unit)

        food.append(new_food)
        food_turtle.goto(new_food)
        food_turtle.dot(15)
def clean_food(ctx):
    food_turtle.color(255, 255, 255)
    print(f"lol: {ctx}")
    food_turtle.goto(ctx)
    food_turtle.dot(16)
    food_turtle.color(0,0,0)





# endregion



async def main():
    global buffered_input
    
    loop_counter = 0
    while True:  
        start_time = time.time() # Get the current time
        
        # Execute your code here
        loop_counter += 1
        turtle.update()
        if loop_counter == 30:
            snake.move(buffered_input, clean_food)
            
            add_food(1, food)
            
            # print(snake.head.pos())
            loop_counter = 0
        
        elapsed_time = time.time() - start_time # Calculate how much time has passed
        delay = max(0.0, 0.001 - elapsed_time) # Calculate how long to delay the loop
        # print(f"delay: {delay}, elapesd time: {elapsed_time}")
        
        time.sleep(delay) # Delay the loop for the calculated time

# region input
buffered_input = snake.heading()

def check_input(input_direction: int) -> bool:
    calc = 180 + input_direction
    if calc >= 360:
        calc = -180 + input_direction
    return calc != snake.heading()
    
    
def handle_input(direction):
    global buffered_input
    if check_input(direction):
        buffered_input = direction

# Call Screen().listen() only once at the beginning of the program
Screen().listen()

# Register the event handlers for key events
Screen().onkey(lambda: handle_input(snake.UP), 'Up')
Screen().onkey(lambda: handle_input(snake.DOWN), 'Down')
Screen().onkey(lambda: handle_input(snake.LEFT), 'Left')
Screen().onkey(lambda: handle_input(snake.RIGHT), 'Right')

# endregion

# Start the main event loop
asyncio.run(main())