from turtle import Turtle, Screen

tur = Turtle()
scr = Screen()

# for i in range(4):
#     tur.forward(100)
#     tur.right(90)
#
# for i in range(20):
#     tur.forward(10)
#     tur.penup()
#     tur.forward(10)
#     tur.pendown()

FULL_CIRCLE = 360
side = 3
angle = FULL_CIRCLE / side

def draw_gon():
    tur.forward(80)
    tur.right(angle)

while side <= 10:
    for i in range(side):
        draw_gon()
    side += 1
    angle = FULL_CIRCLE / side

scr.exitonclick()