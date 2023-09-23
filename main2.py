import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import (AutoLocator, MultipleLocator)
import numpy as np

files = []
for year in range(2007, 2023):
    files.append(pd.read_csv(
        f"data/Seenberichtsdaten Jahr {year}.csv", encoding='ANSI', sep=";", decimal=','))

data = pd.concat(files).drop('PARAMETER', axis=1)
data_lake1 = data[data.MESSSTELLE.str.contains('Vassacher See')]
data_lake2 = data[data.MESSSTELLE.str.contains('Magdalenensee')]
data_lake3 = data[data.MESSSTELLE.str.contains('Silbersee')]

watter_temp_lake1 = data_lake1[data_lake1.PARAMETERBEZEICHNUNG ==
                               'Wassertemperatur'].reset_index(drop=True)

print(watter_temp_lake1)

for xi, yi_min, yi_max in zip(watter_temp_lake1.JAHR, watter_temp_lake1.MIN, watter_temp_lake1.MAX):
    plt.vlines(xi, ymin=yi_min, ymax=yi_max, colors='r',
               linewidth=2, label='Min/Max Values')

plt.plot(watter_temp_lake1.JAHR, watter_temp_lake1.AVG)

plt.minorticks_on()

plt.axis((2006.5, 2022.5, 8, 30,))
plt.xlabel('Year')
plt.ylabel('Water Temperature (°C)')
plt.grid(True, 'both')
plt.show()
