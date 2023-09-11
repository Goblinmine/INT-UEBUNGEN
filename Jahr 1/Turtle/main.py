import turtle, random, colorsys

def gons():
    bob = turtle.Turtle()
    bob.speed(0)
    for i in range(3, 11):
        angle = 360 / (i)
        turtle.Screen().colormode(255)
        bob.color(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
        for _ in range(i):
            bob.forward(100)
            bob.right(angle)
    turtle.Screen().exitonclick()
    
    
def ran_walk():
    bob = turtle.Turtle()
    bob.pensize(5)
    bob.speed(0)
    turtle.Screen().colormode(255)
    
    
    def get_rainbow_color(how_many = 50):
        while True:
            for i in range(how_many):
                hue = i / how_many
                print(hue)
                yield tuple(int(255 * x) for x in colorsys.hsv_to_rgb(hue, 1.0, 1.0))
    
    rainbow = get_rainbow_color(10_000)
    
    while True:
        bob.color(next(rainbow))
        bob.right(random.choice(range(90, 361, 90)))
        bob.forward(10)
        
    
        
ran_walk()