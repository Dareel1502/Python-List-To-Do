#Unit Converter
import tkinter as tk
from PythonCodes import Weight_Converter, Lenght_Converter,Currency_Converter


root = tk.Tk()
root.title("Unit Converter")
root.geometry("300x300")


tk.Button(root, text="Lenght Converter", command=Lenght_Converter.open_window1).pack(pady=10)
tk.Button(root, text= "Weight Converter", command=Weight_Converter.open_window2).pack(pady=10)
tk.Button(root, text= "Currency Converter", command=Currency_Converter.open_window3).pack(pady=10)

root.mainloop()








