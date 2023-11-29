import pandas as panda
import matplotlib.pyplot as pypl
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib import scale as Scale
import math

MST_MAGDALENENSEE = "Magdalenensee" #Konstante für den Magdalenensee
MST_SILBERSEE = "Silbersee" #Konstante für den Silbersee
MST_VASSACHER_SEE = "Vassacher See" #Konstante für den Vassacher See

WERT = "Wassertemperatur" #Konstante für den Wert der Wassertemperatur

data = [] #Liste in der die Daten gespeichert werden
years = [] #Liste in der die Jahre gespeichert werden
temperatures = [] #Liste in der die Temperaturen gespeichert werden
data_kept = [] #für die Daten die offiziel gebraucht werden.

seen = [MST_MAGDALENENSEE, MST_SILBERSEE, MST_VASSACHER_SEE] #Liste in der die Konstanten gespeichert werden

def getNeededData():
    for year in range(2007, 2023): #bestimmt die länge der Jahre von den vorhandenen Files
        years.append(year) #fügt die Jahre in die zuvor erstellte Liste hinzu, die später für die X-Achse benutzt wird
        #liest alle Files mit den Jahren, entschlüsselt es richtig, macht pandas klar das der sepperator ein punktkomma ist
        #und decimal macht die werte automatisch zu einem float, es wird alles der data Liste hinzugefügt
        data.append(panda.read_csv(f"data/Seenberichtsdaten Jahr {year}.csv", encoding='ANSI', sep=";", decimal=','))
        
    for info in data:
        for see in seen:
            mask = info["MESSSTELLE"].str.contains(see)
            removed_rows = info[~mask]
            rows_kept = info.drop(removed_rows.index)
            data_kept.append(rows_kept)
            
    
    return years, data_kept

getNeededData()

#print(years)
#print(data_kept)

def getWatertemperature(sees):
    for temperature in data:
        lake_temperature: panda.DataFrame = temperature[((temperature["PARAMETERBEZEICHNUNG"] == WERT) &(temperature["MESSSTELLE"].str.contains(sees)))]
        temperature_data = lake_temperature["AVG"].to_list()[0]
        temperatures.append(temperature_data)
    return temperatures

#getWatertemperature(MST_VASSACHER_SEE)

#print(temperatures)

def main():
    getNeededData()
    
    y_value = getWatertemperature(MST_MAGDALENENSEE)
    