# Exercise:         squirrel
# Created by:       Jonas Millonig
# Creation date:    18. 09. 2023

import pandas
import numpy as np

data = pandas.read_csv('Jahr 2/Squirrel/data.csv')

print(data.groupby('Primary Fur Color').size().reset_index(name='Amount'))