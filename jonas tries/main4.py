import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np
import random

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

def read_files() -> pd.DataFrame:
    global data
    files = []
    for year in range(2007, 2023):
        files.append(
            pd.read_csv(f"data/Seenberichtsdaten Jahr {year}.csv", 
                        encoding='ANSI', sep=";", decimal=','))
        
    data = pd.concat(files).drop('PARAMETER', axis=1).reset_index(drop=True)


def test(see, parameter) -> pd.DataFrame:
    global data
    return data[
        data.MESSSTELLE.str.contains(see)&
        (data.PARAMETERBEZEICHNUNG == parameter)]




def main():
    global data
    read_files()
    print(data)

main()