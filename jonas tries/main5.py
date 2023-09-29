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
    
    lake_morphometrics = pd.read_csv('data/Seen_Morphometrie.csv', encoding='ANSI', sep=';', decimal=',', thousands='.').set_index('SEE')
    
    
    
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

testingdict: dict

def get_lake_biggest_dif():
    global lake_morphometrics
    
    more = []
    less = []
    
    lake_morphometrics['RELATIVE_ABFLUSS'] = (lake_morphometrics.ABFLUSS / lake_morphometrics.VOLUMEN) * 10000
    lake_morphometrics_sorted = lake_morphometrics.sort_values(by='RELATIVE_ABFLUSS', ascending=False) #[lake_morphometrics.RELATIVE_ABFLUSS.notna()]
    # test = lake_morphometrics[lake_morphometrics.RELATIVE_ABFLUSS.notna()]
    # print(test)
    
    lake_morphometrics_sorted['test'] = np.nan
    
    lake_morphometrics_sorted.loc[lake_morphometrics_sorted['RELATIVE_ABFLUSS'].notna()].head(3)['test'] = True
    lake_morphometrics_sorted.loc[lake_morphometrics_sorted['RELATIVE_ABFLUSS'].notna()].tail(3)['test'] = False
    
    
    # lake_morphometrics_sorted.iloc[:3, -1] = True
    # # lake_morphometrics_sorted.iloc[-3:, -1] = False
    # lake_morphometrics_sorted.loc[lake_morphometrics_sorted.notna(), lake_morphometrics_sorted.columns[1]]
    
    print(lake_morphometrics_sorted)
    
    
    
    
    # testing = lake_morphometrics_sorted[-3:] #.to_dict(orient='index')
    # print(testing)
    
    # for i, lake in lake_morphometrics_sorted[-3:].iterrows():
    #     more.append(i)
    
    # for i, lake in lake_morphometrics_sorted[:3].iterrows():
    #     less.append(i)
    # print(f'more: {more}, less: {less}')


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