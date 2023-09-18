# Exercise:         squirrel
# Created by:       Jonas Millonig
# Creation date:    18. 09. 2023

import pandas
import numpy as np

output = {}
data = pandas.read_csv('Jahr 2/Squirrel/data.csv')

# counting colors
for sqr_color in data['Primary Fur Color']:
    if sqr_color is np.nan: continue
    if sqr_color not in output.keys():
        output[sqr_color] = 1
    else:
        output[sqr_color] += 1

# format into nice csv
export = {
    'color':[],
    'amount':[]
}

for color in output:
    export['color'].append(color)
    export['amount'].append(output[color])

pandas.DataFrame(export).to_csv('Jahr 2/Squirrel/output.csv')