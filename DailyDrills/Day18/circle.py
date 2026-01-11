import turtle
from turtle import Turtle, Screen
from randomwalk import rgb

tur = Turtle()
scr = Screen()
turtle.colormode(255)

tur.speed("fastest")
tur.color("mediumslateblue")
for i in range(100):
    tur.circle(80)
    tur.color(rgb())
    tur.left(10)

scr.exitonclick()