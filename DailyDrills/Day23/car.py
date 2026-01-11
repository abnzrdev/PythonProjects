from turtle import Turtle

class Car(Turtle):
    def __init__(self, color):
        super().__init__()
        self.shape("turtle")
        self.color(color)

    def move(self, speed):
        self.forward(speed)


