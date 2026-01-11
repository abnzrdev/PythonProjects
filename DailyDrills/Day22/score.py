from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = "0"
        self.hideturtle()

    def create_score(self, x_cor, y_cor):
        self.penup()
        self.goto(x_cor, y_cor)
        self.color("white")
        self.write(self.score, font=("Courier", 30, "normal"))

    def increase_score(self):
        self.score = str(int(self.score) + 1)
        self.clear()
        self.write(self.score, font=("Courier", 30, "normal"))