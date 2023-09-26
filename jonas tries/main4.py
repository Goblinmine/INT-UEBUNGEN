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

P_SICHTTIEFE = 'Sichttiefe'
P_WASSERTEMPERATUR = 'Wassertemperatur'
P_PH_WERT = 'pH-Wert'
P_E_LEITFAEIGKEIT = 'Elektrische Leitfähigkeit bei 25°C'
P_PHOSPHOR_GESAMT = 'Phosphor gesamt'
P_NITRAT_STICKSTOFF = 'Nitrat-Stickstoff'
P_SAUERSTOFFGEHALT = 'Sauerstoffgehalt'
P_AMMONIUM_STICKSTOFF = 'Ammonium-Stickstoff'
P_PHYTOPLANKTON_BIOVOLUMEN = 'Phytoplankton Biovolumen'
P_PHOSPHAT_PHOSPHOR = 'Phosphat-Phosphor'

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
        output = data[data.MESSSTELLE.str.contains(f'{MST_MAGDALENENSEE}|{MST_SILBERSEE}|{MST_SILBERSEE}')]
    
    elif see == None and parameter != None:
        output = data[(data.MESSSTELLE.str.contains(f'{MST_MAGDALENENSEE}|{MST_SILBERSEE}|{MST_SILBERSEE}'))&(data.PARAMETERBEZEICHNUNG == parameter)]
    
    elif see != None and parameter == None:
        output = data[data.MESSSTELLE.str.contains(see)]
        
    else:
        output = data[data.MESSSTELLE.str.contains(see)&(data.PARAMETERBEZEICHNUNG == parameter)]
    
    return output.reset_index(drop=True)
    
def show_temp(ax: Axes, title: str):
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
    
    data1 = filter_lake(MST_MAGDALENENSEE, P_WASSERTEMPERATUR)
    color1 = generate_random_color()
    ax[0].plot(data1.JAHR, data1.AVG, label='Average temp', color=color1)
    ax[0].fill_between(data1.JAHR, data1.MAX, data1.MIN, alpha=0.2, label='Min/Max temps', color=color1)
    show_temp(ax[0], 'Magdalenensee')
    
    data2 = filter_lake(MST_SILBERSEE, P_WASSERTEMPERATUR)
    color2 = generate_random_color()
    ax[1].plot(data2.JAHR, data2.AVG, label='Average temp', color=color2)
    ax[1].fill_between(data2.JAHR, data2.MAX, data2.MIN, alpha=0.2, label='Min/Max temps', color=color2)
    show_temp(ax[1], 'Silbersee')
    
    data3 = filter_lake(MST_VASSACHER_SEE, P_WASSERTEMPERATUR)
    color3 = generate_random_color()
    ax[2].plot(data3.JAHR, data3.AVG, label='Average temp', color=color3)
    ax[2].fill_between(data3.JAHR, data3.MAX, data3.MIN, alpha=0.2, label='Min/Max temps', color=color3)
    show_temp(ax[2], 'Vassiacher See')
    
    ax[3].plot(data1.JAHR, data1.AVG, label='Magdalenensee', color=color1)
    ax[3].plot(data2.JAHR, data2.AVG, label='Silbersee', color=color2)
    ax[3].plot(data3.JAHR, data3.AVG, label='Vassiacher See', color=color3)
    show_temp(ax[3], 'ALL')
    
    plt.tight_layout()
    plt.show()
    

main()