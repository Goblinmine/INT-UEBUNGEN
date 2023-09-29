import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib import scale as Scale

MST_MAGDALENSENSEE = "Magdalenensee"
MST_VASSACHER_SEE = "Vassacher See"
MST_SILBERSEE = "Silbersee"

TEMP = "Wassertemperatur"

kept_data = []
years = []
temperatures = []
data = []
seen = [MST_MAGDALENSENSEE, MST_VASSACHER_SEE, MST_SILBERSEE]

def getNeededData():
    for year in range(2007, 2023):
        years.append(year)
        data.append(pd.read_csv(f"data/Seenberichtsdaten Jahr {year}.csv", encoding='ANSI', sep=";", decimal=','))
        
    for info in data:
        for see in seen:
            mask = info["MESSSTELLE"].str.contains(see)
            rows_to_delete = info[~mask]
            rows_to_keep = info.drop(rows_to_delete.index)
            kept_data.append(rows_to_keep)
    return kept_data, years

getNeededData()

def getWaterTemperature():
    for see in kept_data:
        temperature: pd.DataFrame = see[(see["PARAMETERBEZEICHNUNG"] == "Wassertemperatur")]
        temperatur = temperature["AVG"].to_list()[0]
        temperatures.append(temperatur)
    return temperatures

getWaterTemperature()

print(temperatures)