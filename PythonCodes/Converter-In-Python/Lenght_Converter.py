
import tkinter as tk



def open_window1():
    win = tk.Toplevel()
    win.geometry("300x300")
    win.title("Lenght Converter")

    tk.Label(win, text="Length", font=("Arial", 12, "bold")).pack(pady=10)

    centimeter_box = tk.Entry(win, font=("Arial", 12, "bold"))
    centimeter_box.pack(pady=10)
    tk.Label(win, text="Centimeter", font=("Arial", 12, "bold")).pack(pady=10)


    meter_box = tk.Entry(win, font=("Arial", 12, "bold"))
    meter_box.pack(pady=10)
    tk.Label(win, text="Meter ", font=("Arial", 12, "bold")).pack(pady=10)


    meter_label = tk.Label(win, font=("Arial", 12, "bold"))
    meter_label.pack(pady=10)


    centimeter_label = tk.Label(win, font=("Arial", 12, "bold"))
    centimeter_label.pack(pady=10)

    def show_length():
        try:
            if centimeter_box.get() != "":
                centimeter = float(centimeter_box.get())
                meter = centimeter / 100
                meter_label.config(text="In Meter: " + str(round(meter, 2)))

            elif meter_box.get() != "":
                meter = float(meter_box.get())
                centimeter = meter * 100
                centimeter_label.config(text="In Centimeter: " + str(round(centimeter, 2)))

        except ValueError:
            meter_label.config(text="Invalid Input")
            centimeter_label.config(text="Invalid Input")

    submit_button = tk.Button(win, text="Convert", command=show_length)
    submit_button.pack(pady=10)
