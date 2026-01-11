from turtle import Turtle
from constants import HALF_WIDTH, HALF_HEIGHT

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.write_score()

    def write_score(self):
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(HALF_WIDTH - 50, HALF_HEIGHT - 50)
        self.write(self.score, False, "left", ("Consolas", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def relapse(self):
        self.clear()
        self.__init__()