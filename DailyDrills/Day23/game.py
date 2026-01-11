from turtle import Screen
from car import Car
from random import randint
import time

scr = Screen()
cars_color = ["red", "blue", "green", "yellow", "purple", "orange"]
cars = [0] * 6

for i in range(6):
    cars[i] = Car(cars_color[i])
    cars[i].penup()
    cars[i].goto(-300, 250 - i * 100)

scr.tracer(0)

# ==== Game Loop ========
game_over = False
while not game_over:
    time.sleep(0.1)
    scr.update()
    for i in range(6):
        cars[i].move(randint(1,10))
        if cars[i].xcor() >= 300:
            print(f"{cars[i].pencolor()} turtle wins the game.")
            game_over = True


scr.title("Turtle Race Game")
scr.mainloop()