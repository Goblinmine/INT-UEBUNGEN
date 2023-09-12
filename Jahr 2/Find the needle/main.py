# Exercise:         Find the needle
# Created by:       Jonas Millonig
# Creation date:    12. 09. 2023

for i in range(0, 1000):
    with open(f'Jahr 2/Find the needle/needle/{i}.txt') as file:
        if 'needle' in file.read():
            print(f'Needle is in file {i}.txt')
            break