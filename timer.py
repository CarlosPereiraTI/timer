import tkinter as tk

# functions
def start():
    pass

def pause():
    pass

def reset():
    pass


# Window
root = tk.Tk()
root.geometry('400x220')
root.resizable(0,0)
root.title('Timer')


# Clock and buttons
timer_label = tk.Label(text='00:00:00', font=('Calibri', 70))
timer_label.pack()

start_button = tk.Button(text='Start', height=2, width=7, font=('Calibri', 15), command=start)
start_button.pack(side=tk.LEFT, padx=10, pady=10)

pause_button = tk.Button(text='Pause', height=2, width=7, font=('Calibri', 15), command=pause)
pause_button.pack(side=tk.LEFT, padx=10, pady=10)

reset_button = tk.Button(text='Reset', height=2, width=7, font=('Calibri', 15), command=reset)
reset_button.pack(side=tk.LEFT, padx=10, pady=10)

close_button = tk.Button(text='Close', height=2, width=7, font=('Calibri', 15), command=root.quit)
close_button.pack(side=tk.LEFT, padx=10, pady=10)

root.mainloop()