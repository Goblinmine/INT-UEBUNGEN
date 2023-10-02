import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib import scale as Scale
import math

MST_MAGDALENSENSEE = "Magdalenensee"
MST_VASSACHER_SEE = "Vassacher See"
MST_SILBERSEE = "Silbersee"

TEMP = "Wassertemperatur"

kept_data = []
years = []
temperatures = []
data = []
y_values = []
seen = [MST_MAGDALENSENSEE, MST_VASSACHER_SEE, MST_SILBERSEE]

def getNeededData():
    global seen
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
#print(kept_data)

def getWaterTemperature(See):
    for seas in data:
        temperature: pd.DataFrame = seas[((seas["PARAMETERBEZEICHNUNG"] == TEMP) & (seas["MESSSTELLE"].str.contains(See)))] #
        temperatur = temperature["AVG"].to_list()[0]
        temperatures.append(temperatur)
    #print(temperatures)
    return temperatures

#getWaterTemperature(MST_SILBERSEE)

#print(temperatures)

def getYvalues():
    for sees in data:
        y_val: pd.DataFrame = sees[((sees["PARAMETERBEZEICHNUNG"] == TEMP)& sees["MESSSTELLE"].str.contains(MST_MAGDALENSENSEE))] #       
        y_value = y_val["AVG"].to_list()[0]
        y_values.append(y_value)
    return y_values

#getYvalues()
#print(y_values)

def main():
    getNeededData()
    getYvalues()
    
    x_range = range(2007, years[-1]+1)
    y_range = range(0, int(math.ceil(max(y_values)+1)))
    
    fig, ax = plt.subplots()
    
    ax: Axes
    
    ax.set_xlim(years[0], years[-1])
    ax.set_xticks(x_range)
    ax.set_xticklabels(x_range, rotation= 45)
    
    ax.set_ylim(y_values[0], y_values[-1])
    ax.set_yticks(y_range)
    
    maggalenensee_temperature = getWaterTemperature(MST_MAGDALENSENSEE)
    silbersee_temperature = getWaterTemperature(MST_SILBERSEE)
    vassacher_see_temperature = getWaterTemperature(MST_VASSACHER_SEE)
    
    ax.plot(years, maggalenensee_temperature, label="Magdalenensee")
    ax.plot(years,  silbersee_temperature, label="Silbersee")
    ax.plot(years,  vassacher_see_temperature, label="Vassacher See")
    
    ax.legend(loc = "lower right", ncols = 3)
    ax.set_title("Wassertemperatur")
    ax.set_xlabel("Jahre")
    ax.set_ylabel("AVG-Temperatur (C°)")
    ax.grid(visible= True)
    
    plt.show()
    
main()