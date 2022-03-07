# # with open("./DAY25/weather_data.csv") as weather:
# #     data = weather.readlines()
# # print(data)

# # import csv
# # from itertools import count 

# # with open('./DAY25/weather_data.csv') as weather:

# #     data = csv.reader(weather)

# #     tempreture = []

# #     for row in data:
# #         if row[1] != 'temp':
# #             tempreture.append(int(row[1]))
# #     print(tempreture)

# import pandas

# data = pandas.read_csv('./DAY25/weather_data.csv')
# # temp = data['temp'].max()
# # print(temp)

# # print(data[data.day =='Monday'])

# # max_row = data[data.temp == data['temp'].max()]
# # print(max_row)
# f = 33.8
# d = data[data.day == "Monday"]
# print((d.temp *2)+30) 

from numpy import pad
import pandas

data = pandas.read_csv("DAY25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_color_count = len(data[data['Primary Fur Color'] == "Gray"])
cinnamon_color_count = len(data[data['Primary Fur Color'] == "Cinnamon"])
black_color_count = len(data[data['Primary Fur Color'] == "Black"])

print(gray_color_count)

print(cinnamon_color_count)

print(black_color_count)

data_dict = {

            "Fur Colors":['Gray','Cinnamon','Black'],
            "Count":[gray_color_count,cinnamon_color_count,black_color_count]
}

new_data=pandas.DataFrame(data_dict)
new_data.to_csv("DAY25/squirrel_count.csv")

