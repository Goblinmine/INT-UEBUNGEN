from turtle import Turtle, Screen
import colorsys

Screen().colormode(255)

def get_rainbow_color(how_many = 50):
        while True:
            for i in range(how_many):
                hue = i / how_many
                yield tuple(int(255 * x) for x in colorsys.hsv_to_rgb(hue, 1.0, 1.0))
    
rainbow = get_rainbow_color(200)

class Snake:
    UP = 90
    DOWN = 270
    RIGHT = 0
    LEFT = 180
    
    __body_pos = []
    __body_stamps = []
    __food: list[tuple[int, int]]
    head: Turtle
    grow = False
    
    __grid_size = 20
    
    def __init__(self, food: list[tuple[int, int]], start_size = 3) -> None:
        # get ref. of food list
        self.__food = food
        self.head = Turtle('square')
        self.head.penup()
        self.head.speed(0)
        self.__build(start_size)
        # self.head.shapesize()
    
    
    # how to eat? get array with food. if snake head on same possition eat. remove food. grow snake
    
    # needs multible chcks.
    # 1. in contact with food?
    # 2. need to grow?
    # 3. in conntact with itself?
    # 4. won?
    
    
    def __check_food(self):
        pos = (
            int(self.head.pos()[0]),
            int(self.head.pos()[1])
        )
        if pos in self.__food:
            self.__food.remove(pos)
            self.grow = True
            
    
    def heading(self):
        return self.head.heading()
    
    def move(self, heading: int):
        self.__check_food()
        print(f"Turtle: {self.head.pos()}, foods: {self.__food}")
        self.head.setheading(heading)
        self.__body_stamps.append(self.head.stamp())
        self.head.forward(self.__grid_size)
        self.head.color(next(rainbow))
        
        # if i want to grow then do not clear stamp
        if self.grow:
            self.grow = False
            return
            
        self.head.clearstamp(self.__body_stamps.pop(0))
    
    def __build(self, size = 3):
        size -= 1
        self.head.back(size*self.__grid_size)
        for _ in range(size):
            self.grow = True
            self.move(self.RIGHT)