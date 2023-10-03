import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np
import random
import colorsys
import re

lake_data: pd.DataFrame
lake_morphometrics: pd.DataFrame

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


def generate_random_color():
    h = random.uniform(0, 1)
    s = random.uniform(0.8, 1)
    l = random.uniform(0.4, 0.6)
    return colorsys.hls_to_rgb(h, l, s)

testingdict: dict


def get_lake_biggest_dif(num:int = 3):
    global lake_morphometrics
    lake_morphometrics['RELATIVE_ABFLUSS'] = (lake_morphometrics.ABFLUSS / lake_morphometrics.VOLUMEN) * 10000
    output = lake_morphometrics.sort_values(by='RELATIVE_ABFLUSS', ascending=False)
    # return output.head(num), output.tail(num)
    return output.join(get_phytoplankton()).dropna(subset=['RELATIVE_ABFLUSS', 'AVG_Phytoplankton'])
    

def get_phytoplankton():
    global lake_data
    output = pd.DataFrame(columns=['AVG_Phytoplankton'])
    for row in lake_data[lake_data.PARAMETERBEZEICHNUNG == 'Phytoplankton Biovolumen'][['MESSSTELLE', 'AVG']].itertuples():
        # See if lake allready entry. if not add entry. if true then calc avg
        messstelle = re.sub(' [\[\(].*[\]\)]', '', row[1])
        if messstelle in output.index:
            output.loc[messstelle] = output.loc[messstelle].AVG_Phytoplankton / 2
        else:
            output.loc[messstelle] = [row[2]]
            
    return output

def main():  
    read_files()
    output = get_lake_biggest_dif()
    ax: Axes
    fig, ax = plt.subplots(layout='constrained')
    plt.suptitle('Title', fontsize=16)
    print(output)
    
    # output[['RELATIVE_ABFLUSS', 'AVG_Phytoplankton']].to_csv("output.csv")
    
    
    
    ax.plot(output.RELATIVE_ABFLUSS, output.AVG_Phytoplankton, marker='o', linestyle='')
    ax.set_xticks(output.RELATIVE_ABFLUSS)
    ax.set_xticklabels(output.index.tolist(), rotation=90)
    ax.set_xlabel('Relativer Abfluss (l/s/m³ * 10000)')
    ax.set_ylabel('AVG Phytoplankton Biovolumen (mm³/l)')
    plt.show()
    
    
main()
    
    
# def test():
#     read_files()
#     output = get_lake_biggest_dif()
#     print(output)
#     ax: Axes
#     fig, ax = plt.subplots(layout='constrained')
#     plt.suptitle('Title', fontsize=16)
    
#     x = np.arange(len(output))  # the label locations
#     width = 0.25  # the width of the bars
#     multiplier = 0


#     for row in output[['RELATIVE_ABFLUSS', 'AVG_Phytoplankton']].itertuples():
#         offset = width * multiplier
#         rects = ax.bar(x + offset, row[1], width, label=row[1])
#         # ax.bar_label(rects, padding=3)
#         multiplier += 1
        
#     # Add some text for labels, title and custom x-axis tick labels, etc.
#     ax.set_ylabel('Length (mm)')
#     ax.set_title('Penguin attributes by species')
#     ax.set_xticks(x + width, output.index.tolist())
#     ax.legend(loc='upper left', ncols=3)
#     # ax.set_ylim(0, 250)

#     plt.show()
    

    
# test()