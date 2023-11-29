import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np
import random

VASSACHER_SEE = 'Vassacher See'
MAGDALENENSEE = 'Magdalenensee'
SILBERSEE = 'Silbersee'

data: pd.DataFrame

def read_data():
    global data
    files = []
    for year in range(2007, 2023):
        files.append(pd.read_csv(
            f"data/Seenberichtsdaten Jahr {year}.csv", encoding='ANSI', sep=";", decimal=','))
    data = pd.concat(files).drop('PARAMETER', axis=1).reset_index(drop=True)
    
    
    # data_lake1 = data[data.MESSSTELLE.str.contains('Vassacher See')]
    # data_lake2 = data[data.MESSSTELLE.str.contains('Magdalenensee')]
    # data_lake3 = data[data.MESSSTELLE.str.contains('Silbersee')]

    # watter_temp_lake1 = data_lake1[data_lake1.PARAMETERBEZEICHNUNG ==
    #                             'Wassertemperatur'].reset_index(drop=True)
    # watter_temp_lake2 = data_lake2[data_lake2.PARAMETERBEZEICHNUNG ==
    #                             'Wassertemperatur'].reset_index(drop=True)
    # watter_temp_lake3 = data_lake3[data_lake3.PARAMETERBEZEICHNUNG ==
    #                             'Wassertemperatur'].reset_index(drop=True)

    # lakes = {
    #     'Vassacher See':watter_temp_lake1,
    #     'Magdalenensee':watter_temp_lake2,
    #     'Silbersee':watter_temp_lake3
    # }

    # print(watter_temp_lake1)
    
def filter_lake_data(lake, parameter):
    global data
    output = data[data.MESSSTELLE.str.contains(lake)]
    if parameter == None: return output.reset_index(drop=True)
    return output[output.PARAMETERBEZEICHNUNG.str.contains(parameter)].reset_index(drop=True)
    
    
def main():
    read_data()
    print(filter_lake_data(MAGDALENENSEE, 'Sichttiefe'))
    pass

main()




# fig: Figure


# def flaten_nd_array(nd_list) -> list[Axes]:
#     output = []
#     for item in nd_list.flat:
#         output.append(item)
#     return output


# fig, nd_ax = plt.subplots(2,2, figsize=(10,6))
# ax = flaten_nd_array(nd_ax)

# # Find the global minimum and maximum values for the y-axis
# global_min = min(lakes[lake_name].MIN.min() for lake_name in lakes)
# global_max = max(lakes[lake_name].MAX.max() for lake_name in lakes)

# # Iterate over lakes
# for i, lake_name in enumerate(lakes):
#     color = (random.randint(0,10)/10,random.randint(0,10)/10,random.randint(0,10)/10,)
    
#     ax[i].set_title(lake_name)
#     ax[i].plot(lakes[lake_name].JAHR, lakes[lake_name].AVG, color=color)
#     ax[i].fill_between(lakes[lake_name].JAHR, lakes[lake_name].MAX, lakes[lake_name].MIN, alpha=0.2, color=color)
    
#     # Set the same y-axis limits for all axes
#     ax[i].set_ylim(global_min, global_max)
    
#     # Customize x-axis ticks and labels
#     ax[i].set_xticks(range(2007, 2023))  # Set ticks every 2 years
#     ax[i].set_xticklabels([str(tick) for tick in range(2007, 2023)], rotation=45)  # Set tick labels and rotate them for readability
    
#     ax[i].grid(True)
#     ax[i].minorticks_on()
#     ax[i].grid(True, axis='y', which='minor', linestyle='--', alpha=0.2)
#     ax[i].set_xlabel("Year")
#     ax[i].set_ylabel("Temperature (°C)")
    
#     test = ax[i]
    
#     for i, j in zip(lakes[lake_name].JAHR, lakes[lake_name].AVG):
#         test.annotate(f'{j}', (i, j), textcoords='offset points', xytext=(0,-30), ha='center')
        

# plt.tight_layout()
# plt.show()

# for i, lake_name, in zip(range(0, 3), lakes):
#     ax[i].set_title(lake_name)
#     ax[i].plot(lakes[lake_name].JAHR, lakes[lake_name].AVG)
#     ax[i].fill_between(lakes[lake_name].JAHR, lakes[lake_name].MAX, lakes[lake_name].MIN, alpha=0.2)
#     ax[i].set_xticks(range(2007,2023))
#     ax[i].grid(True)
#     ax[i].set_xlabel("Year")
#     ax[i].set_ylabel("Temperature (°C)")
        




# x, y1, y_max1, y_min1 = watter_temp_lake1.JAHR, watter_temp_lake1.AVG, watter_temp_lake1.MIN, watter_temp_lake1.MAX
# y2, y_max2, y_min2 = watter_temp_lake2.AVG, watter_temp_lake2.MIN, watter_temp_lake2.MAX
# y3, y_max3, y_min3 = watter_temp_lake3.AVG, watter_temp_lake3.MIN, watter_temp_lake3.MAX

# ax.plot(x, y1, color='r')
# ax.plot(x, y_max1, 'o', color='r')
# ax.plot(x, y_min1, 'o', color='r')

# ax.plot(x, y2, color='b')
# ax.plot(x, y_max2, 'o', color='b')
# ax.plot(x, y_min2, 'o', color='b')

# ax.plot(x, y3, color='y')
# ax.plot(x, y_max3, 'o', color='y')
# ax.plot(x, y_min3, 'o', color='y')

# # ax.fill_between(x1, y_max1, y_min1, alpha=0.1)
# # ax.fill_between(x2, y_max2, y_min2, alpha=0.1)
# # ax.fill_between(x3, y_max3, y_min3, alpha=0.1)

# ax.set_xlim(2006.5, 2022.5)
# ax.set_ylim(8, 30)
# ax.set_xlabel('Year')
# ax.set_ylabel('Water Temperature (°C)')

# ax.grid(True)


# plt.show()

# for xi, yi_min, yi_max in zip(x, y_min, y_max):
#     ax.vlines(xi, yi_min, yi_max, colors='r',
#                linewidth=2, label='Min/Max Values')

# ax.plot(x, y)

# ax.minorticks_on()

# ax.set_xlim(2006.5, 2022.5)
# ax.set_ylim(8, 30)
# ax.set_xlabel('Year')
# ax.set_ylabel('Water Temperature (°C)')
# ax.grid(True, which='both')

# plt.show()