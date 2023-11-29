import pandas 
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib import scale as Scale
data = pandas.read_csv("data/Seen_Morphometrie.csv", encoding='ANSI', sep=";")
# print(data)

myFiles = []
years = []
#label_names = [ "Magdalenensee", "Vassacher See", "Silbersee"]
for year in range(2007, 2023):
    myFiles.append(pandas.read_csv(
        f"data/Seenberichtsdaten Jahr {year}.csv", encoding='ANSI', sep=";", decimal=','))
    years.append(year)

for dataFrame in myFiles:
    mask = dataFrame['MESSSTELLE'].str.contains('Magdalenensee|Vassacher See|Silbersee')
    rowsToDelete = dataFrame[~mask]
    RowsWeNeed = dataFrame.drop(rowsToDelete.index)
    #print(RowsWeNeed)


see1 = {
    "Wassertemperatur": [],
    "Sichttiefe": [],
    "ph-Wert": [],
    "Elektr. Leitfaehigkeit": [],
    "Phosphor": [],
    "Nitrat-Stickstoff": [],
    "Ammonium-Stickstoff": [],
    "Sauerstoffgehalt": [],
    "Phytoplankton Biovolumen": [],
    "Chlorid": [],
    "Chlorophyll": []}

see2 = {
    "Wassertemperatur": [],
    "Sichttiefe": [],
    "ph-Wert": [],
    "Elektr. Leitfaehigkeit": [],
    "Phosphor": [],
    "Nitrat-Stickstoff": [],
    "Ammonium-Stickstoff": [],
    "Sauerstoffgehalt": [],
    "Phytoplankton Biovolumen": [],
    "Chlorid": [],
    "Chlorophyll": []}

see3 = {
    "Wassertemperatur": [],
    "Sichttiefe": [],
    "ph-Wert": [],
    "Elektr. Leitfaehigkeit": [],
    "Phosphor": [],
    "Nitrat-Stickstoff": [],
    "Ammonium-Stickstoff": [],
    "Sauerstoffgehalt": [],
    "Phytoplankton Biovolumen": [],
    "Chlorid": [],
    "Chlorophyll": []}

# see1 = {
#     "Wassertemperatur": [],
#     }



for year_data in myFiles:
    # alle rows drinen
    data_filterd: pandas.DataFrame = year_data[(year_data["PARAMETERBEZEICHNUNG"] == "Wassertemperatur") & (year_data["MESSSTELLE"].str.contains("Magdalenensee"))]
    data_wasser_temp = data_filterd["AVG"].to_list()[0]
    see1['Wassertemperatur'].append(data_wasser_temp)
print(see1)

for year_data_one in myFiles:
    second_data_filtered: pandas.DataFrame = year_data_one[(year_data_one["PARAMETERBEZEICHNUNG"] == "Wassertemperatur") & (year_data_one["MESSSTELLE"].str.contains("Vassacher See"))]
    second_data_wasser_temp = second_data_filtered["AVG"].to_list()[0]
    see2["Wassertemperatur"].append(second_data_wasser_temp)
print(see2)

for year_data_two in myFiles:
    third_data_filtered: pandas.DataFrame = year_data_two[(year_data_two["PARAMETERBEZEICHNUNG"] == "Wassertemperatur") & (year_data_two["MESSSTELLE"].str.contains("Silbersee"))]
    third_data_wasser_temp = third_data_filtered["AVG"].to_list()[0]
    see3["Wassertemperatur"].append(third_data_wasser_temp)
print(see3)
ax: Axes

fig, ax = plt.subplots()

x_range = range(years[0], years[-1]+1)
y_range = range(0, int(max(see1["Wassertemperatur"])+1))

ax.set_xlim(years[0], years[-1])
ax.set_xticks(x_range)
ax.set_xticklabels(x_range, rotation=45)

ax.set_ylim(see1["Wassertemperatur"][0], see1["Wassertemperatur"][-1])
ax.set_yticks(y_range)

ax.plot(years, see1['Wassertemperatur'], label ="Magdalenensee" )
ax.plot(years, see2['Wassertemperatur'], label="Vassacher See" , color= "#7D3C98")
ax.plot(years, see3['Wassertemperatur'], label= "Silbersee" , color="#2ECC71")

ax.legend(loc = "lower right", ncols = 3)
ax.set_title("Wassertemperatur")
ax.set_xlabel("Jahre")
ax.set_ylabel("AVG-Temperatur (C°)")
ax.grid(visible= True)

plt.show()