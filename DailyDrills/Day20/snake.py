from turtle import Turtle

class Snake(Turtle):
    """Represents and manages the snake in the game."""

    def __init__(self):
        super().__init__()
        self.segments = []
        starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        for position in starting_positions:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)
        self.head = self.segments[0]
        self.length_of_snake = len(self.segments)


    def move(self):

        """
            Moves the snake forward by updating the position of each segment.
            Args: None
        """

        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(10)

    def change_direction(self, direction):

        """
        Changes the direction of the snake's head.
        Args:
            direction (str): "right", "left", "up", "down"
        """

        if direction == "right" and self.head.heading() != 180:
            self.head.setheading(0)
        elif direction == "left" and self.head.heading() != 0:
            self.head.setheading(180)
        elif direction == "up" and self.head.heading() != 270:
            self.head.setheading(90)
        elif direction == "down" and self.head.heading() != 90:
            self.head.setheading(270)

    def grow_snake(self):

        """
        Adds a new segment to the end of the snake.
        Args: None
        """

        x_cor = self.segments[self.length_of_snake - 1].xcor() - 20
        y_cor = self.segments[self.length_of_snake - 1].ycor() - 20
        add_segment = Turtle("square")
        add_segment.color("white")
        add_segment.penup()
        add_segment.goto(x_cor, y_cor)
        self.segments.append(add_segment)

    # TODO: IMPLEMENT THE COLLISION LOGIC SEPARATELY CAUSE THERE IS NO WAY TO HECK IT THE SHORTER DISTANCE OTHER THAN THIS AND READ ABOUT IT IN CHATGPT
    def collision_action(self):
        """Resets the snake by hiding all segments and reinitializing.

        Args: None
        """

        for segment in self.segments:
            segment.hideturtle()
        self.__init__()




