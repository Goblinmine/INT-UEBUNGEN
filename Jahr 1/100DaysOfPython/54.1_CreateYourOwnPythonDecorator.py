# Exercise:         Day 54.1 | Create Your Own Python Decorator
# Created by:       Jonas Millonig
# Creation date:    01.03.2023

import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(function, dec = 2):
    start_time = time.time()
    function()
    stop_time = time.time()
    speed = round(stop_time - start_time, dec)
    return f"{function.__name__} run speed: {speed}s"
    
def fast_function():
    for i in range(10000000):
        i * i
        
def slow_function():
    for i in range(100000000):
        i * i
        
      
      
print(speed_calc_decorator(fast_function, 5))
print(speed_calc_decorator(slow_function))
    