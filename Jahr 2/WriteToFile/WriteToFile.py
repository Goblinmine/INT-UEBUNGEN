# Exercise:         Write To File
# Created by:       Jonas Millonig
# Creation date:    12. 09. 2023

rootPath = 'Jahr 2/WriteToFile/'

# with open(rootPath + 'myFile.txt') as file:
    # contents = file.read()
    # print(contents)

with open(rootPath + 'myFile.txt', 'w') as file:
    file.write('New text.')