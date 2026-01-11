# Reading data from csv
# with open("weather_data.csv", 'r') as weather_data:
#     data = weather_data.readlines()

# the above just normal way of do just as a file but working with that type
# will be hard when we are continuing to work on it
# and there is a library to work with those files

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)  # this will return iterable object
#     tempratures = []
#     for row in data:    # We are iterating through the object
#         if(row[1] != "temp"):
#             tempratures.append(int(row[1]))

# Better than all of those there is one better way in reading datas which is massive library
# with robust features
import pandas
# data = pandas.read_csv("weather_data.csv")
# temprature = data["temp"]
# temp_list = data["temp"].to_list()
# sum = 0;
# for temp in temp_list:
#     sum += temp
#
# average = sum / len(temp_list)
# print(average)

# those all above work can be done just by using some other ways in panda
# finding the row of the maximum
# max_temp = data.temp.max()
# print(data[data.temp == max_temp])

# there are two types of data type in pandas (this is good thing to know in every libraries)
# then those data types are known as series(column) and data frame (2dimensional row X column)
# key is the column then the value will be row then after filtering the value using some ways
# then that will also be some kind of data type

# monday = data[data.day == "Monday"]
# monday_fah_temp = (monday.temp * 1.8) + 32;
# print(monday_fah_temp)

# Creating a data frame from scratch
# data_dict = {
#     "students" : ["Amy" , "James", "Angela"],
#     "scores" : [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

#this helps us to create data frame by our self too like changing some kind of objects to pandas as it has
# a lot of things to do by itself






# =========== Squirel Data ===========
sq_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color = sq_data["Primary Fur Color"]
color_counts = color.value_counts().to_dict()
color_df = pandas.DataFrame(color_counts.items(), columns=["Fur Color", "Count"])
color_df.to_csv("squirrel_count.csv", index=False)
