#Creating a Temperature Converter

import tkinter as tk

def show_temp():
  try:
    if celsius_box.get() !="":
        celsius = float(celsius_box.get())
        fahrenheit = (celsius * 9 / 5) + 32
        fahrenheit_label.config(text="In Fahrenheit" + str(round(fahrenheit, 2)))

    elif fahrenheit_box.get() !="":
        fahrenheit = float(fahrenheit_box.get())
        celsius = (fahrenheit - 32) * 5/9
        celsius_label.config(text="In Celsius: " + str(round(celsius, 2)))

  except ValueError:
      celsius_label.config(text="Invalid Input")
      fahrenheit_label.config(text="Invalid Input")

root = tk.Tk()
root.geometry("400x300")
root.title("Temperature Converter")

tk.Label(root, text="Temperature", font=("Arial", 12, "bold")).pack(pady=10)

fahrenheit_box= tk.Entry(root, width=20,  font=("Arial", 12, "bold"))
fahrenheit_box.pack(pady=10)
tk.Label(root, text="Fahrenheit").pack()

celsius_box = tk.Entry(root, width=20, font=("Arial", 12, "bold"))
celsius_box.pack(pady=10)
tk.Label(root, text="Celsius").pack()


submit_button = tk.Button(root, text="Convert", command=show_temp, font=("Arial", 12, "bold", "italic"))
submit_button.pack(pady=10)

celsius_label = tk.Label(root, text="", fg="white", bg="black" , font=("Arial", 12))
celsius_label.pack(padx=5, pady=5)

fahrenheit_label = tk.Label(root, text="", fg="white", bg="black", font=("Arial", 12))
fahrenheit_label.pack(padx=5, pady=5)

root.mainloop()








