from turtle import Screen
from snake import Snake
from food import Food
from score import Score
from constants import *
import time

# Setting up scree
scr = Screen()
scr.setup(WIDTH, HEIGHT)
scr.bgcolor("black")              #to make the game utilities visible
scr.tracer(0)

# Defining Instances
snk = Snake()
food = Food()
score = Score()

# Tweaking Instances
scr.listen()

## Defining Event listeners
scr.onkeypress(lambda : snk.change_direction(direction="up") , key="Up")
scr.onkeypress(lambda : snk.change_direction(direction="down") , key="Down")
scr.onkeypress(lambda : snk.change_direction(direction="right") , key="Right")
scr.onkeypress(lambda : snk.change_direction(direction="left"), key="Left")

# Game Condition checkers
def check_collision():
    if snk.head.xcor() + (SNAKE_HEAD_WIDTH / 2) >= HALF_WIDTH or snk.head.xcor() - (SNAKE_HEAD_WIDTH / 2) <= HALF_NEG_WIDTH:
        return True
    if snk.head.ycor() + (SNAKE_HEAD_WIDTH / 2) >= HALF_HEIGHT or snk.head.ycor() - (SNAKE_HEAD_WIDTH / 2) <= HALF_NEG_HEIGHT:
        return True

    snk.head.pos = (snk.head.xcor(), snk.head.ycor())
    snk.body_positions = [(segment.xcor(), segment.ycor()) for segment in snk.segments[1:]]
    if snk.head.pos in snk.body_positions:
        return True

    return False
# Main Game loop
while True:

    # Conditions of the game
    if snk.head.distance(food) < 20:
        food.spawn()
        snk.grow_snake()
        score.increase_score()

    if check_collision():
        snk.collision_action()
        score.relapse()

    snk.move()
    scr.update()
    time.sleep(0.05)
scr.exitonclick()