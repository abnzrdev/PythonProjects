from turtle import *


tur = Turtle()
scr = Screen()

# Tweaking the screen
scr.title("Etch Sketch")
scr.bgcolor("black")
scr.listen()

tur.pensize(3)
tur.pencolor("white")
tur.speed(0)
tur.hideturtle()

def moveforward():
    x_cor = tur.xcor()
    tur.setx(x_cor + 10)

def moveback():
    x_cor = tur.xcor()
    tur.setx(x_cor - 10)

def moveup():
    y_cor = tur.ycor()
    tur.sety(y_cor + 10)

def movedown():
    y_cor = tur.ycor()
    tur.sety(y_cor - 10)

def upper_right_curve():
    tur.pendown()
    tur.circle(30,20)

def upper_left_curve():
    tur.pendown()
    tur.circle(-30,20)

def turn_red():
    tur.pencolor("red")

def clear():
    tur.clear()
    tur.penup()
    tur.home()
    tur.pendown()

scr.onkeypress(fun=moveforward, key="Right")
scr.onkeypress(fun=moveback, key="Left")
scr.onkeypress(fun=moveup, key="Up")
scr.onkeypress(fun=movedown, key="Down")
scr.onkeypress(fun=upper_right_curve, key="d")
scr.onkeypress(fun=upper_left_curve, key="h")
scr.onkey(fun=clear, key="c")
scr.onkey(fun=turn_red, key="r")

scr.exitonclick()