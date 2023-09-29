import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np
import random
import colorsys

data: pd.DataFrame

MST_VASSACHER_SEE = 'Vassacher See'
MST_MAGDALENENSEE = 'Magdalenensee'
MST_SILBERSEE = 'Silbersee'

MST_MYLAKES = f'{MST_MAGDALENENSEE}|{MST_VASSACHER_SEE}|{MST_SILBERSEE}'

P_WASSERTEMPERATUR = 'Wassertemperatur'

def read_files():
    global data
    files = []
    for year in range(2007, 2023):
        files.append(
            pd.read_csv(f"data/Seenberichtsdaten Jahr {year}.csv", 
                        encoding='ANSI', sep=";", decimal=','))
        
    data = pd.concat(files).drop('PARAMETER', axis=1).reset_index(drop=True)


def filter_lake(see = None, parameter = None) -> pd.DataFrame:
    global data
    output = None
    
    if see == None and parameter == None:
        output = data[data.MESSSTELLE.str.contains(MST_MYLAKES)]
    
    elif see == None and parameter != None:
        output = data[(data.MESSSTELLE.str.contains(MST_MYLAKES))&(data.PARAMETERBEZEICHNUNG == parameter)]
    
    elif see != None and parameter == None:
        output = data[data.MESSSTELLE.str.contains(see)]
        
    else:
        output = data[data.MESSSTELLE.str.contains(see)&(data.PARAMETERBEZEICHNUNG == parameter)]
    
    return output.reset_index(drop=True)

def format_plot(ax: Axes, title: str):
    lake_data = filter_lake(parameter=P_WASSERTEMPERATUR)
    ax.set_ylim(0, lake_data.MAX.max() + 1) # take from every lake
    x_ticks = range(lake_data.JAHR.min(), lake_data.JAHR.max() + 1)
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_ticks, rotation=45)
    ax.grid(True)
    ax.minorticks_on()
    ax.grid(True, axis='y', which='minor', alpha=0.2)
    ax.set_xlabel('Year')
    ax.set_ylabel('Temperature (°C)')
    ax.legend(loc='lower left')
    ax.set_title(title)
    
def show_temp(ax: Axes, title: str, lakename: str) -> tuple[pd.DataFrame, tuple[float, float, float]]:
    data = filter_lake(lakename, P_WASSERTEMPERATUR)
    color = generate_random_color()
    ax.plot(data.JAHR, data.AVG, label='Average temp', color=color)
    ax.fill_between(data.JAHR, data.MAX, data.MIN, alpha=0.2, label='Min/Max temps', color=color)
    format_plot(ax, title)
    return data, color
    

def flaten_nd_array(nd_list) -> list[Axes]:
    output = []
    for item in nd_list.flat:
        output.append(item)
    return output


def generate_random_color():
    h = random.uniform(0, 1)
    s = random.uniform(0.8, 1)
    l = random.uniform(0.4, 0.6)
    return colorsys.hls_to_rgb(h, l, s)        

def main():
    global data
    read_files()
    
    fig: Figure
    
    fig, nd_ax = plt.subplots(2,2, figsize=(10,10))
    ax = flaten_nd_array(nd_ax)
    
    fig.suptitle('Water temps from 2007 until 2022 for 3 lakes.', fontsize=16)
    
    data_lake1 = show_temp(ax[0], 'Magdalenensee', MST_MAGDALENENSEE)
    data_lake2 = show_temp(ax[1], 'Silbersee', MST_SILBERSEE)
    data_lake3 = show_temp(ax[2], 'Vassiacher See', MST_VASSACHER_SEE)
    
    ax[3].plot(data_lake1[0].JAHR, data_lake1[0].AVG, label='Magdalenensee', color=data_lake1[1])
    ax[3].plot(data_lake2[0].JAHR, data_lake2[0].AVG, label='Silbersee', color=data_lake2[1])
    ax[3].plot(data_lake3[0].JAHR, data_lake3[0].AVG, label='Vassiacher See', color=data_lake3[1])
    format_plot(ax[3], 'ALL')
    
    plt.tight_layout()
    plt.show()
    
main()