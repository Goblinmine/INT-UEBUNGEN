# Exercise:         Pandas
# Created by:       Jonas Millonig
# Creation date:    18. 09. 2023
 
import pandas

# data = pandas.read_csv("Jahr 2/Pandas/wather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(len(temp_list))

# print(data["temp"].mean())
# print(data['temp'].max())
# print(data[data.day == 'Monday'])

# monday = data[data.day == "Monday"]
# print((monday.temp * 9 / 5 + 32))


data_dict = {
    'students':['jonas', 'peter','fritz'],
    'scores': [20, 50, 12]
}

data = pandas.DataFrame(data_dict)
data.to_csv('Jahr 2/Pandas/new_data.csv')