import turtle
from turtle import Turtle, Screen
from random import random, choice, randint

color_list = [
    "mediumslateblue", "darkorchid", "deepskyblue", "springgreen", "goldenrod", "firebrick",
    "dodgerblue", "mediumvioletred", "aquamarine", "chartreuse", "slategray", "rosybrown",
    "mediumturquoise", "palegreen", "lightcoral", "darkkhaki", "mediumseagreen", "indianred",
    "peachpuff", "mistyrose", "lightsteelblue", "cadetblue", "mediumaquamarine", "peru",
    "lightseagreen", "powderblue", "seagreen", "burlywood", "darkslateblue", "mediumspringgreen",
    "paleturquoise", "darkgoldenrod", "mediumblue", "orchid", "plum", "sienna", "skyblue",
    "thistle", "tomato", "wheat"
]
directions = [0,90,180,270]
# Using the rgb color scheme
def rgb():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    color = (r,g,b)
    return color

def randomwalk():
    tur = Turtle()
    scr = Screen()
    tur.pensize(10)
    turtle.colormode(255)
    for i in range(400):

        tur.forward(50)
        tur.setheading(choice(directions))
        tur.color(rgb())

if __name__ == "__main__":
    randomwalk()
    scr.exitonclick()