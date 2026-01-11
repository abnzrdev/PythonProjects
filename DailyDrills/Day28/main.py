from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
ACTIVE_GREEN = "#7ccf9b"
ACTIVE_RED = "#d94b5b"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_minute = math.floor(count / 60)
    count_second = count % 60
    if count_second < 10:
        count_second = f"0{count_second}"

    canvas.itemconfig(timer_text, text=f"{count_minute} : {count_second}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.resizable(False, False)

# Timer text
timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

# Canvas with the tomato image and centered timer text
tomato_img = PhotoImage(file='tomato.png')
canvas = Canvas(width=tomato_img.width(), height=tomato_img.height(), bg=YELLOW, highlightthickness=0)
canvas.create_image(tomato_img.width() // 2, tomato_img.height() // 2, image=tomato_img)
timer_text = canvas.create_text(tomato_img.width() // 2, tomato_img.height() // 2 + 20, text="25:00", fill="white",
                       font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
canvas.image = tomato_img  # Prevent garbage collection

# buttons for controlling
start_button = Button(
    text="Start",
    font=(FONT_NAME, 14, "bold"),
    bg=GREEN, fg="white",
    activebackground=ACTIVE_GREEN, activeforeground="white",
    bd=0, highlightthickness=0,
    padx=24, pady=8,
    cursor="hand2",
    command=start_timer
)
start_button.grid(column=0, row=2, pady=(20, 0))

reset_button = Button(
    text="Reset",
    font=(FONT_NAME, 14, "bold"),
    bg=RED, fg="white",
    activebackground=ACTIVE_RED, activeforeground="white",
    bd=0, highlightthickness=0,
    padx=24, pady=8,
    cursor="hand2",
    command=reset_timer
)
reset_button.grid(column=2, row=2, pady=(20, 0))

# Check Marks
check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()

