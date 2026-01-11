import turtle
from turtle import *
from random import choice

tur = Turtle()
scr = Screen()
turtle.colormode(255)
tur.speed("slowest")

colors = [(238, 224, 203), (204, 157, 106), (172, 71, 36),
          (233, 216, 224), (217, 218, 226), (227, 208, 117),
          (141, 145, 160), (95, 104, 135), (192, 151, 170),
          (183, 152, 41), (223, 229, 224), (32, 34, 14),
          (19, 26, 61), (97, 115, 173), (221, 172, 195),
          (173, 28, 9), (22, 36, 20), (121, 105, 113),
          (197, 98, 74), (234, 174, 160), (144, 151, 146),
          (101, 109, 103), (41, 51, 100), (182, 184, 214),
          (172, 104, 122), (46, 29, 45), (73, 72, 41),
          (232, 203, 16), (121, 38, 50), (55, 71, 54)]

count = 0


tur.penup()
tur.goto(-100,-100)

for i in range(10):
    for j in range(10):
        tur.color(choice(colors))
        tur.dot(10)
        tur.penup()
        if j < 9:
            tur.forward(30)
    if i < 9:
        if count % 2 == 0:
            tur.left(90)
            tur.penup()
            tur.forward(30)
            tur.dot(10)
            tur.left(90)
        else:
            tur.right(90)
            tur.penup()
            tur.forward(30)
            tur.dot(10)
            tur.right(90)
    count += 1

scr.exitonclick()