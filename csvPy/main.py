# with open("weather_data.csv") as file:
#     data = file.readlines()
#
# print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] == 'temp':
#             continue
#         temperatures.append(int(row[1]))
#     print(temperatures)

# data = pd.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# print(data[data["temp"] == data["temp"].max()])

import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_sqrl_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_sqrl_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_sqrl_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color":["Gray", "Cinnamon", "Black"],
    "count": [gray_sqrl_count, cinnamon_sqrl_count, black_sqrl_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("sqrl_count.csv")
