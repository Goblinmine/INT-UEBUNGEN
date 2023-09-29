import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np
import random
import colorsys

lake_data: pd.DataFrame
lake_morphometrics: pd.DataFrame

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
    global lake_data
    global lake_morphometrics
    files = []
    for year in range(2007, 2023):
        files.append(
            pd.read_csv(f"data/Seenberichtsdaten Jahr {year}.csv", 
                        encoding='ANSI', sep=";", decimal=','))
        
    lake_data = pd.concat(files).drop('PARAMETER', axis=1).reset_index(drop=True)
    
    lake_morphometrics = pd.read_csv('data/Seen_Morphometrie.csv', encoding='ANSI', sep=';', decimal=',', thousands='.')
    
    
    
def filter_lake(see = None, parameter = None) -> pd.DataFrame:
    global lake_data
    output = None
    
    if see == None and parameter == None:
        output = lake_data[lake_data.MESSSTELLE.str.contains(f'{MST_MAGDALENENSEE}|{MST_SILBERSEE}|{MST_SILBERSEE}')]
    
    elif see == None and parameter != None:
        output = lake_data[(lake_data.MESSSTELLE.str.contains(f'{MST_MAGDALENENSEE}|{MST_SILBERSEE}|{MST_SILBERSEE}'))&(lake_data.PARAMETERBEZEICHNUNG == parameter)]
    
    elif see != None and parameter == None:
        output = lake_data[lake_data.MESSSTELLE.str.contains(see)]
        
    else:
        output = lake_data[lake_data.MESSSTELLE.str.contains(see)&(lake_data.PARAMETERBEZEICHNUNG == parameter)]
    
    return output.reset_index(drop=True)


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


def get_lake_biggest_dif():
    global lake_morphometrics
    # test = lake_morphometrics[lake_morphometrics.ABFLUSS]
    
    # df = df[df['EPS'].notna()]
    
    lake_morphometrics['AVG'] = lake_morphometrics.ABFLUSS / lake_morphometrics.VOLUMEN * 1000
    
    print(lake_morphometrics)
    
    test1 = lake_morphometrics.sort_values(by='ABFLUSS')[lake_morphometrics.ABFLUSS.notna()].reset_index(drop=True)
    
    test2 = test1[-3:]
    test3 = test1[:3]
    
    print(test1)
    print(test2)
    print(test3)
    
    # test2 = lake_morphometrics[lake_morphometrics.SEE == 'Wörthersee'].VOLUMEN
    
    # print(test1)
    # print(test2)


def main():
    global lake_data
    global lake_morphometrics
    
    read_files()
    
    get_lake_biggest_dif()
    
    fig: Figure
    
    fig, nd_ax = plt.subplots(2,2, figsize=(10,10))
    ax = flaten_nd_array(nd_ax)
    
    fig.suptitle('Title', fontsize=16)
    
    plt.show()
    
main()