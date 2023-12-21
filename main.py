from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
LIGHT_MAROON = "#EAB2A0"
LIGHT_PURPLE = "#6D67E4"
LIGHT_BLUE = "#A3C7D6"
NIGHT_BLUE = "#092635"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_mark = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #


def timer_reset():
    global reps
    global check_mark
    window.after_cancel(timer)
    reps = 0
    check_mark = ""
    check.config(text=check_mark)
    label1.config(text="Timer")
    canvas.itemconfig(text_count, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    global check_mark
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label1.config(text="Long Break", bg=NIGHT_BLUE, fg=LIGHT_MAROON, font=(FONT_NAME, 50))
        check_mark += "✔"
        check.config(text=check_mark)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label1.config(text="Short Break", bg=NIGHT_BLUE, fg=LIGHT_PURPLE, font=(FONT_NAME, 50))
        check_mark += "✔"
        check.config(text=check_mark)
    else:
        count_down(work_sec)
        label1.config(text="Work", bg=NIGHT_BLUE, fg=LIGHT_BLUE, font=(FONT_NAME, 50))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        new_count = f"0{count_sec}"
        count_sec = new_count

    canvas.itemconfig(text_count, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

# Windows
window = Tk()
window.title("Pomodoro Timer - Moon's Version")
window.config(padx=50, pady=30, bg=NIGHT_BLUE)

# Canvas
moon_image = PhotoImage(file="imagens/moon_ed.png")
canvas = Canvas(width=550, height=450, bg=NIGHT_BLUE, highlightthickness=0)
canvas.create_image(275, 245, image=moon_image)
text_count = canvas.create_text(275, 245, text="00:00", font=(FONT_NAME, 34, "bold"),
                                fill="black")
canvas.grid(column=2, row=2)

# Buttons
start = PhotoImage(file="imagens/start_bt.png")
reset = PhotoImage(file="imagens/reset_bt.png")
start_bt = Button(window, image=start,
                  text="Start",
                  border=0,
                  bg=NIGHT_BLUE,
                  fg=NIGHT_BLUE,
                  command=start_timer)
start_bt.config(activebackground=NIGHT_BLUE)
start_bt.grid(column=0, row=3)
reset_bt = Button(window, image=reset, text="Reset", border=0, bg=NIGHT_BLUE, fg=NIGHT_BLUE, command=timer_reset)
reset_bt.config(activebackground=NIGHT_BLUE)
reset_bt.grid(column=3, row=3)

# Labels
label1 = Label(text="Timer", bg=NIGHT_BLUE, fg=LIGHT_BLUE, font=(FONT_NAME, 50))
label1.grid(column=2, row=0)
check = Label(bg=NIGHT_BLUE, fg=LIGHT_BLUE, font=(FONT_NAME, 22))
check.grid(column=2, row=4)

window.mainloop()
