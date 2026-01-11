# Some ways just for dictionary comprhension

inp = input("Write the text : ")
word_counter = {word: len(word) for word in inp.split()}
print(word_counter)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day: (1.8 * temp + 32) for day, temp in weather_c.items()}
print(weather_f)