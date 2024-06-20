"""
Class Battery:
has a function that time is passed on and then the the green square bar size increases
and lets

"""

import tkinter as tk
import time

OUTLINE_WIDTH = 100
OUTLINE_HEIGHTS = 50
CHARGE_WIDTH = 90
CHARGE_HEIGHTS = 40
INC_TIME = 6000  # 6 sec increment time between every bettery updates


class TimerBattery:
    def __init__(self, window):
        self.x_adj = 0
        self.window = window
        self.canvas = tk.Canvas(self.window, bg="black", height=60, width=120, highlightthickness=0)
        self.canvas.grid(column=0, row=7)

        #battery outline
        self.bat_outline = self.canvas.create_rectangle(5, 5, 105, 55, outline="white", width=3)
        self.battery_terminal = self.canvas.create_rectangle(105, 20, 115, 40, fill="white")
        #self.battery_fill = self.canvas.create_rectangle(10, 10, 10, 50, outline="", fill="green")
        #self.state = "work"  #work or break state
        #self.start_timer(timer_len = 3)

    def battery_starter(self, timer_len):
        #updating the rectangle to zero zero
        self.battery_fill = self.canvas.create_rectangle(10, 10, 10, 50, outline="", fill="green")
        #self.canvas.coords(self.battery_fill, 10, 10, 10, 50)
        self.new_x = 10
        self.update_battery(timer_len)
        self.x_adj = int(90/timer_len)

    def update_battery(self, timer_len):
        if timer_len >= 0:
            self.new_x += self.x_adj
            self.canvas.coords(self.battery_fill, 10, 10, self.new_x, 50)  #draws a new rectangle
            timer_len -= 1
            self.window.after(INC_TIME, self.update_battery, timer_len)  #calls itself back until the timer_len gets to 0


class FullBattery:
    def __init__(self, window):
        self.window = window
        self.batShape = tk.Canvas(self.window)
