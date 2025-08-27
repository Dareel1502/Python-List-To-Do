# Simple Digital Clock
#Import the tkinter which can be used as a Python GUI
import tkinter as tk
from time import strftime

#Define a function to show the time
def time():
    string = strftime("%I:%M:%S %p")
    label.config(text=string)
    label.after(1000, time)

#The main Window
root = tk.Tk()
root.title("Digital Clock")

#Label to show the clock
label = tk.Label(root, font=("Arial", 35), fg="cyan", bg="black")
label.pack(anchor="center")

#Start the Clock to Run
time()
root.mainloop()

