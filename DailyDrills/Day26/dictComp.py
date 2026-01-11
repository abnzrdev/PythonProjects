# Dictionary comprhension
import random
names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank']
fidx = {name: random.randint(40,100) for name in names}
passed_students = {name : score for name, score in fidx.items() if score > 50}
print(fidx)
print(passed_students)
