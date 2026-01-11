from turtle import Screen, Turtle
from bar import Bar
from ball import Ball
from score import Score

# Defining the screen boundaries as tuples
HORIZONTAL_LIMIT = (-300, 300)  # (left, right)
VERTICAL_LIMIT = (-300, 300)    # (bottom, top)

# Creating the screen of game
scr = Screen()
scr.bgcolor("black")
scr.setup((HORIZONTAL_LIMIT[1] - HORIZONTAL_LIMIT[0]), (VERTICAL_LIMIT[1] - VERTICAL_LIMIT[0]))
scr.listen()

# Game Utilities
player = Bar()
computer = Bar()
player_score = Score()
computer_score = Score()
playing_ball = Ball()

# Event listeners
scr.onkeypress(fun=lambda: player.move_bar_up() if player.ycor() < VERTICAL_LIMIT[1] - 30 else None, key="Up")
scr.onkeypress(fun=lambda: player.move_bar_down() if player.ycor() > VERTICAL_LIMIT[0] + 30 else None, key="Down")
scr.onkeypress(fun=lambda: computer.move_bar_up() if computer.ycor() < VERTICAL_LIMIT[1] - 30 else None, key="w")
scr.onkeypress(fun=lambda: computer.move_bar_down() if computer.ycor() > VERTICAL_LIMIT[0] + 30 else None, key="s")

# ---- First game state ---- run as soon as the program run
def starting_part():

    # Creating the middle dash
    dash = Turtle()
    dash.speed("fastest")
    dash.hideturtle()
    for y in range(-280, 300, 40):
        dash.penup()
        dash.pensize(2)
        dash.goto(0, y)
        dash.pendown()
        dash.pencolor("white")
        dash.setheading(270)
        dash.forward(20)
        dash.penup()

    # Positioning the player
    player.create_bar(HORIZONTAL_LIMIT[0] + 20, 0)
    computer.create_bar(HORIZONTAL_LIMIT[1] - 20, 0)

    # Positioning the score
    player_score.create_score(x_cor=-70, y_cor=230)
    computer_score.create_score(x_cor=50, y_cor=230)

    # Positioning the ball
    playing_ball.create_ball()

# Relapse the game
def relapse_game():
    playing_ball.hideturtle()
    playing_ball.goto(0, 0)
    playing_ball.showturtle()

# Collision Logic with the bar
def is_collision(ball, bar):
    ball_x, ball_y = ball.xcor(), ball.ycor()
    bar_x, bar_y = bar.xcor(), bar.ycor()
    bar_width = 20  # adjusted width of the bar
    bar_height = 60 # adjusted height of the bar
    ball_radius = 10  # default ball's radius

    return (bar_x - bar_width/2 - ball_radius < ball_x < bar_x + bar_width/2 + ball_radius and
            bar_y - bar_height/2 - ball_radius < ball_y < bar_y + bar_height/2 + ball_radius)

# Game Loop -- Middle part -----
def game_loop():cle
    while int(player_score.score) < 10 and int(computer_score.score) < 10:
        # Colliding with the bar
        if is_collision(playing_ball, player) or is_collision(playing_ball, computer):
            playing_ball.bounce_x()
            print("collide")

        # Colliding with the upper and lower limits of the screen
        if not (VERTICAL_LIMIT[0] + 10 < playing_ball.ycor() < VERTICAL_LIMIT[1] - 10):
            print("Colliding with the vertical bar")
            playing_ball.bounce_y()

        # Score Increment
        if playing_ball.xcor() > HORIZONTAL_LIMIT[1]:
            player_score.increase_score()
            relapse_game()
        if playing_ball.xcor() < HORIZONTAL_LIMIT[0]:
            computer_score.increase_score()
            relapse_game()

        playing_ball.move()

# do not run when imported it will run when executed
starting_part()
game_loop()

scr.exitonclick()