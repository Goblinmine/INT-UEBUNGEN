import pandas as pd
import matplotlib.pyplot as plt

files = []
for year in range(2007, 2023):
    files.append(pd.read_csv(f"data/Seenberichtsdaten Jahr {year}.csv", encoding='ANSI', sep=";"))

data = pd.concat(files).drop('PARAMETER', axis=1)
data_lake1 = data[data.MESSSTELLE.str.contains('Vassacher See')]
data_lake2 = data[data.MESSSTELLE.str.contains('Magdalenensee')]
data_lake3 = data[data.MESSSTELLE.str.contains('Silbersee')]

watter_temp_lake1 = data_lake1[data_lake1.PARAMETERBEZEICHNUNG == 'Wassertemperatur']

plt.plot(watter_temp_lake1.JAHR, watter_temp_lake1.AVG)

# Adding axis labels and customizing their font size
plt.xlabel('Date', fontsize=15)
plt.ylabel('Rate', fontsize=15)
plt.yscale('linear')

plt.show()

# print(data_lake1, data_lake2, data_lake3)