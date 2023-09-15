# Exercise:         Read csv
# Created by:       Jonas Millonig
# Creation date:    15. 09. 2023

# import csv

path = 'Jahr 2/Read csv/weather_data.csv'

# with open(path) as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp": 
#             temperatures.append(int(row[1]))
#     print(temperatures)


import pandas

data = pandas.read_csv(path)

print(data['temp'])