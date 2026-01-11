from turtle import Turtle, Screen
import random

# Create a screen for the turtle graphics
scr = Screen()
scr.setup(600,600)


# This code creates a simple turtle five instances with different colors.
tur1 = Turtle()
tur1.shape("turtle")
tur1.color("red")
tur1.penup()
tur1.goto(-490,0)
tur1.pensize()

tur2 = Turtle()
tur2.shape("turtle")
tur2.color("blue")
tur2.penup()
tur2.goto(-490,30)

tur3 = Turtle()
tur3.shape("turtle")
tur3.color("green")
tur3.penup()
tur3.goto(-490,-30)

tur4 = Turtle()
tur4.shape("turtle")
tur4.color("orange")
tur4.penup()
tur4.goto(-490,60)

tur5 = Turtle()
tur5.shape("turtle")
tur5.color("purple")
tur5.penup()
tur5.goto(-490,-60)

# Creating a bet with the user
user_choice = input("Which one will win : ")

while True:
    tur1.forward(random.randint(1, 10))
    tur2.forward(random.randint(1, 10))
    tur3.forward(random.randint(1, 10))
    tur4.forward(random.randint(1, 10))
    tur5.forward(random.randint(1, 10))

    if tur1.xcor() >= 590:
        print("Red turtle wins!")
        break
    elif tur2.xcor() >= 590:
        print("Blue turtle wins!")
        break
    elif tur3.xcor() >= 590:
        print("Green turtle wins!")
        break
    elif tur4.xcor() >= 590:
        print("Orange turtle wins!")
        break
    elif tur5.xcor() >= 590:
        print("Purple turtle wins!")
        break

scr.exitonclick()