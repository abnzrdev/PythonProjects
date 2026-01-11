from random import randint
from turtle import Turtle
from constants import *

class Food(Turtle):

    """Represents the food object in the snake game."""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.spawn()

    def spawn(self):

        """Places the food at a random position within screen bounds.

        Args: None
        """
        x_cor = randint(HALF_NEG_WIDTH + BALL_DIAMETER, HALF_WIDTH - BALL_DIAMETER)
        y_cor = randint(HALF_NEG_HEIGHT + BALL_DIAMETER, HALF_HEIGHT - BALL_DIAMETER)
        self.penup()
        self.goto(x_cor, y_cor)
