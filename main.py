from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    windows.after_cancel(timer)
    timer_label.config(text="Timer")
    check_mark_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global rep
    rep = rep + 1

    work_sec = WORK_MIN*60
    short_rest_sec = SHORT_BREAK_MIN*60
    long_rest_sec = LONG_BREAK_MIN*60

    if rep % 8 == 0:
        down_count(long_rest_sec)
        timer_label.config(text= "Break", fg=RED)
    elif rep % 2 == 0:
        down_count(short_rest_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        down_count(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def down_count(count):
    global timer
    now = time.strftime('%M:%S', time.gmtime(count))
    canvas.itemconfig(timer_text, text=now)
    if count > 0:
        timer = windows.after(1000, down_count, count-1)
    else:
        start_timer()
        work_session = math.floor(rep/2)
        marks = ""
        for _ in range(work_session):
            marks += "✔"
            check_mark_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.title("pomodoro")
windows.config(padx=100, pady=100, bg=YELLOW)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
image_file = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image_file)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)


#lables

timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 36, "bold"), bg=YELLOW)
timer_label.grid(column=1, row=0)

check_mark_label = Label(fg=GREEN, bg=YELLOW)
check_mark_label.grid(column=1, row=3)


#button
start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)


windows.mainloop()