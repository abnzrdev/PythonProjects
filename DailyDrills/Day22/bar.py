from turtle import Turtle

class Bar(Turtle):
    def __init__(self):
        super().__init__()

    def create_bar(self, x_cor, y_cor):
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=3, stretch_len=1)
        self.goto(x_cor, y_cor)

    def move_bar_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 10
            self.goto(self.xcor(), new_y)

    def move_bar_down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)

