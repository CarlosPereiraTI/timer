from cProfile import run
import tkinter as tk
from turtle import update
from tkinter import *


# Window
root = tk.Tk()
root.geometry('400x220')
root.resizable(0,0)
photo = PhotoImage(file="clock.png")
root.iconphoto(True, photo)
root.title(' My Break')


# variables
running = False
hours = 0
minutes = 0
seconds = 0


# functions
def start():
    global running
    if not running:
        update()
        running = True


def pause():
    global running
    if running:
        timer_label.after_cancel(update_time)
        running = False


def reset():
    global running
    if running:
        timer_label.after_cancel(update_time)
        running = False

    global hours, minutes, seconds
    hours = 0
    minutes = 0
    seconds = 0

    timer_label.config(text='00:00:00')


# update stopwatch function
def update():
    global hours, minutes, seconds
    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 30 and seconds == 1:
        # hours += 1
        # minutes = 0
        pause()
        tk.messagebox.showwarning(title="My Break", message="Alert: Your break has finished.")

    # format time 
    hours_string = f'{hours}' if hours > 9 else f'0{hours}'
    minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
    seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'
    # update timer label after 1 second
    timer_label.config(text=hours_string + ':' + minutes_string + ':' + seconds_string)
    # timer_label.config(minutes_string + ':' + seconds_string)
    # use update_time variable to cancel or pause the time using after_cancel
    global update_time
    update_time = timer_label.after(1000, update)


# Clock and buttons
timer_label = tk.Label(text='00:00:00', font=('Calibri', 80))
timer_label.pack()

start_button = tk.Button(text='Start', height=2, width=7, font=('Calibri', 15), command=start)
start_button.pack(side=tk.LEFT, padx=10, pady=10)
pause_button = tk.Button(text='Pause', height=2, width=7, font=('Calibri', 15), command=pause)
pause_button.pack(side=tk.LEFT, padx=10, pady=10)
# reset_button = tk.Button(text='Reset', height=2, width=7, font=('Calibri', 15), command=reset)
# reset_button.pack(side=tk.LEFT, padx=10, pady=10)
close_button = tk.Button(text='Close', height=2, width=7, font=('Calibri', 15), command=root.quit)
close_button.pack(side=tk.RIGHT, padx=10, pady=10)

root.mainloop()