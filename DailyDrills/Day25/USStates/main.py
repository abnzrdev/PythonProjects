# ===============================================
# WRITTEN BY: ABENEZER
# US STATES GUESSING GAME WITH 10-MINUTE TIMER
# ===============================================

# Import libraries: turtle for graphics/map display, pandas for CSV data handling, time for timer functionality
import turtle
import pandas as pd
import time

# ===============================================
# GAME SETUP AND SCREEN CONFIGURATION
# ===============================================

screen = turtle.Screen()
screen.title("State Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.bgpic(image)

# ===============================================
# TIMER SETUP AND DISPLAY
# ===============================================

GAME_TIME = 600  # 10 minutes in seconds
start_time = time.time()
timer_turtle = turtle.Turtle()
timer_turtle.hideturtle()
timer_turtle.penup()
timer_turtle.goto(-350, 250)
timer_turtle.color("red")


def update_timer():
    elapsed = time.time() - start_time
    remaining = max(0, GAME_TIME - elapsed)
    minutes = int(remaining // 60)
    seconds = int(remaining % 60)
    timer_turtle.clear()
    timer_turtle.write(f"Time: {minutes:02d}:{seconds:02d}", font=("Arial", 16, "bold"))
    return remaining > 0


# ===============================================
# USER INPUT HANDLING FUNCTION
# ===============================================

def get_user_guess():
    answer = screen.textinput(title="Guess the State",
                              prompt="What's another state's name?")
    return answer


# ===============================================
# DATA LOADING AND PREPARATION
# ===============================================

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()

# ===============================================
# STATE PLACEMENT FUNCTION
# ===============================================

def place_state_on_map(state_name):
    state_data = data[data.state == state_name]
    if not state_data.empty:
        x = int(state_data.x.iloc[0])
        y = int(state_data.y.iloc[0])
        state_turtle = turtle.Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()
        state_turtle.goto(x, y)
        state_turtle.write(state_name)


# ===============================================
# MAIN GAME LOGIC AND LOOP WITH TIMER
# ===============================================

game_is_on = True
guessed_states = []
end_reason = None  # 'completed', 'timeout', 'exit'

while game_is_on:
    if not update_timer():
        end_reason = 'timeout'
        game_is_on = False
        break

    screen.title(f"{len(guessed_states)}/50 States Correct")
    user_answer = get_user_guess()

    if user_answer is None or user_answer.lower() == 'exit':
        end_reason = 'exit'
        game_is_on = False
        break

    user_answer = user_answer.title()

    if user_answer in all_states and user_answer not in guessed_states:
        guessed_states.append(user_answer)
        place_state_on_map(user_answer)

    if len(guessed_states) == 50:
        end_reason = 'completed'
        game_is_on = False
        screen.title("Congratulations! You got all 50 states!")

# ===============================================
# GAME ENDING AND FINAL SCORE DISPLAY
# ===============================================

elapsed_total = time.time() - start_time
minutes_played = int(elapsed_total // 60)
seconds_played = int(elapsed_total % 60)

game_over_turtle = turtle.Turtle()
game_over_turtle.hideturtle()
game_over_turtle.penup()
game_over_turtle.goto(0, 0)

if end_reason == 'completed':
    message = f"Amazing! You got all 50 states in {minutes_played}:{seconds_played:02d}!"
elif end_reason == 'exit':
    message = f"You exited. You guessed {len(guessed_states)} out of 50."
elif end_reason == 'timeout':
    message = f"Time's up! You guessed {len(guessed_states)} out of 50 in 10 minutes."
else:
    message = f"Game ended. Score: {len(guessed_states)}/50."

game_over_turtle.write(message, align="center", font=("Arial", 16, "bold"))

screen.exitonclick()
