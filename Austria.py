austria = {
    "Burgenland" : {"Einwohner": 284900,
                    "Flaeche": 3961.8,
                    "Hauptstadt": {"Name": "Eisenstadt", "Einwohner": 14476},
                    "Landeshauptmann": "Hans Peter Doskozil"},
    "Steiermark" : {"Einwohner": 1210700,
                    "Flaeche": 16401.04,
                    "Hauptstadt": {"Name": "Graz", "Einwohner": 286292},
                    "Landeshauptmann": "Hermann Schützenhöfer"},
    "Niederösterreich" : {"Einwohner": 1612000,
                    "Flaeche": 19186.26,
                    "Hauptstadt": {"Name": "St. Pölten", "Einwohner": 54649},
                    "Landeshauptmann": "Johanna Mikl-Leitner"},
    "Oberösterreich" : {"Einwohner": 1412700,
                    "Flaeche": 11979.91,
                    "Hauptstadt": {"Name": "Linz", "Einwohner": 204846},
                    "Landeshauptmann": "Thomas Stelzer"},
    "Salzburg" : {"Einwohner": 531800,
                    "Flaeche": 7156.03,
                    "Hauptstadt": {"Name": "Salzburg", "Einwohner": 153377},
                    "Landeshauptmann": "Wilfried Haslauer"},
    "Tirol" : {"Einwohner": 710100,
                    "Flaeche": 12640.17,
                    "Hauptstadt": {"Name": "Innsbruck", "Einwohner": 132493},
                    "Landeshauptmann": "Günther Platter"},
    "Vorarlberg" : {"Einwohner": 370800,
                    "Flaeche": 2601.12,
                    "Hauptstadt": {"Name": "Bregenz", "Einwohner": 29806},
                    "Landeshauptmann": "Markus Wallner"},
    "Kärnten" : {"Einwohner": 558300,
                    "Flaeche": 9538.01,
                    "Hauptstadt": {"Name": "Klagenfurt", "Einwohner": 100369},
                    "Landeshauptmann": "Peter Kaiser"},
    "Wien" : {"Einwohner": 1888776,
                    "Flaeche": 414.65,
                    "Hauptstadt": {"Name": "Wien", "Einwohner": 1888776},
                    "Landeshauptmann": "Michael Ludwig"}
}


# fix Landeshauptmänner
austria['Steiermark']['Landeshauptmann'] = 'Cristopher Drexter'
austria['Tirol']['Landeshauptmann'] = 'Anton Mattle'

m
# print(austria.keys())

for key in austria:
    print(key)

for key, value in austria.items():
    print(f'{key}: {value["Einwohner"]} Einwohner')
    
for key, value in austria.items():
    print(f'{key}: Hauptstadt: {value["Hauptstadt"]["Name"]}')