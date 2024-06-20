from tkinter import *
from battery import TimerBattery

# ---------------------------- CONSTANTS ------------------------------- #

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
Rep = 0


def start_session():
    myBattery.battery_starter(timer_len=int(work_time.get()))


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title(" Mental Battery")
window.config(padx=100, pady=50, background="black")

work_label = Label(text="work time (min)")
work_label.grid(column=0, row=0)
work_time = Entry(width=10)
work_time.grid(column=0, row=1)

break_label = Label(text="break time (min)")
break_label.grid(column=0, row=2)
break_time = Entry(width=10)
break_time.grid(column=0, row=3)

rounds_label = Label(text="rounds")
rounds_label.grid(column=0, row=4)
rounds = Entry(width=10)
rounds.grid(column=0, row=5)

myBattery = TimerBattery(window)

start_button = Button(text="Start", command=start_session)
start_button.grid(column=0, row=6)

window.mainloop()
