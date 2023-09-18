# Exercise:         squirrel
# Created by:       Jonas Millonig
# Creation date:    18. 09. 2023

import pandas
import numpy as np

# Read csv file
data = pandas.read_csv('Jahr 2/Squirrel/data.csv')

# only show relevant data and group by color
data_filterd = data.groupby('Primary Fur Color').size().reset_index(name='Amount')

# save data to csv file
data_filterd.to_csv('Jahr 2/Squirrel/output.csv')