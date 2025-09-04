import tkinter as tk

def open_window2():
    win = tk.Toplevel()
    win.title("Weight Converter")
    win.geometry("400x300")

    tk.Label(win, text="Weight Converter", font=("Arial", 12, "bold")).pack(pady=10)


    kilogram_box = tk.Entry(win, font=("Arial", 12, "bold"))
    kilogram_box.pack(pady=10)
    tk.Label(win, text="Kilogram", font=("Arial", 12, "bold")).pack(pady=10)

    pound_box = tk.Entry(win, font=("Arial", 12, "bold"))
    pound_box.pack(pady=10)
    tk.Label(win, text="Pound", font=("Arial", 12, "bold")).pack(pady=10)



    pound_label = tk.Label(win,  font=("Arial", 12, "bold"))
    pound_label.pack(pady=10)

    kilogram_label = tk.Label(win,font=("Arial", 12, "bold"))
    kilogram_label.pack(pady=10)

    def show_wieght():
        try:
            if pound_box.get() != "":
                pound = float(pound_box.get())
                kilogram = pound * 0.45
                kilogram_label.config(text="In Kilograms " + str(round(kilogram, 2)))

            elif kilogram_box.get() != "":
                kilogram = float(kilogram_box.get())
                pound = kilogram * 2.20
                pound_label.config(text="In Pound " + str(round(pound, 2)))

        except ValueError:
            pound_label.config(text="Please enter a number.")
            kilogram_label.config(text="Please enter a number.")

    submit_button = tk.Button(win, text="Submit", command=show_wieght)
    submit_button.pack(pady=10)












