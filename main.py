import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv("data/Seen_Morphometrie.csv", encoding='ANSI', sep=";")
# print(data)

myFiles = []
years = []

for year in range(2007, 2023):
    myFiles.append(pandas.read_csv(
        f"data/Seenberichtsdaten Jahr {year}.csv", encoding='ANSI', sep=";"))
    years.append(year)

for dataFrames in myFiles:
    mask = dataFrames['MESSSTELLE'].str.contains(
        'Magdalenensee|Vassacher See|Silbersee')
    rowsToDelete = dataFrames[~mask]
    deletedRows = dataFrames.drop(rowsToDelete.index)
    # print(deletedRows)


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


# print(years)
year07 = myFiles[0]
mask = (year07['MESSSTELLE'].str.contains('Magdalenensee')) & (
    year07["PARAMETERBEZEICHNUNG"] == "Wassertemperatur")
see1["Wassertemperatur"] = mask
print(see1)
# print(year07[mask])

# rowsToDelete = year07[~mask]

# test = year07.drop(rowsToDelete.index)

# print(test)
# DELETE FROM data WHERE Messstelle != nameSee
