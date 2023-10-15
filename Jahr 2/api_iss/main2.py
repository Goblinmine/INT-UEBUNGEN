import main as api
import turtle
import time

def setup_turtle():
    screen = turtle.Screen()
    screen.setup(1000,500)
    screen.bgpic('Jahr 2/api_iss/earth.gif')
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.addshape('Jahr 2/api_iss/iss.gif')
    iss = turtle.Turtle()
    iss.shape('Jahr 2/api_iss/iss.gif')
    iss.penup()
    
    return screen, iss


def my_loop(iss: turtle.Turtle):
    # get current iss position
    iss_lat, iss_lng = api.get_iss_position()
    iss.goto(iss_lng,iss_lat)
    iss.pendown()


def main():
    screen, iss = setup_turtle()
    while True:
        my_loop(iss)
        time.sleep(2)


if __name__ == '__main__':
    main()

# def main():
#     # LAT = 46.636459
#     # LNG = 14.312225
#     LAT = 16
#     LNG = -87
   
#     try:
#         if not api.is_night(LAT, LNG):
#             exit()
        
#         if api.iss_overhead(LAT, LNG):
#             print('ISS is over your head!!')
            
#     except Exception as ex:
#         print(f'ERROR: {ex}')

