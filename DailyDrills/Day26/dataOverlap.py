with open("first.txt", "r") as first:
    first_nums = first.readlines()

with open("second.txt", "r") as second:
    second_nums = second.readlines()

both = [int(num) for num in first_nums if num in second_nums]
print(both)