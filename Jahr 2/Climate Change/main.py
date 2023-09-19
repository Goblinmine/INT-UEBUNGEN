import pandas as pd

root_path = 'Jahr 2/Climate Change/'

data = pd.read_csv(root_path+'data/Seenberichtsdaten Jahr 2007.csv', encoding='ANSI', sep=';')
print(data)