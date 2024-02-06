# with open("weather_data.csv") as weather:
#     data = weather.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as weather:
#     data = csv.reader(weather)
#     print(data)
#     temp = []
#     for row in data:
#         if row[1] != "temp":
#             temp.append(int(row[1]))
#     print(temp)
#     # for row in data:
#     #     print(row)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(type(data["temp"]))
# print(type(data))

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)
print(len(temp_list))

# avg_tmp = 0
# tot_tmp = 0
# for i in temp_list:
#     tot_tmp += i
#
# avg_tmp = tot_tmp / len(temp_list)
# print(avg_tmp)

# avg = sum(temp_list) / len(temp_list)
# print(avg)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # Get Data in columns
# print(data["condition"])
# print(data.condition)

# Get Data in Row
print(data[data.day == "Monday"])

# Get Data in Row that had max temp
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
print(monday.condition)
print(monday_temp * 9/5 +32)

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
print(data)
