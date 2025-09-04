import tkinter as tk




def open_window3():
   win = tk.Toplevel()
   win.title("Currency Converter")
   win.geometry("400x300")

   tk.Label(win, text="Currency Converter",font=("Arial", 12, "bold") ).pack(pady=10)


   peso_box = tk.Entry(win, font=("Arial", 12, "bold"))
   peso_box.pack(pady=10)
   tk.Label(win, text="Peso ", font=("Arial", 12, "bold")).pack(pady=10)

   dollar_box = tk.Entry(win, font=("Arial", 12, "bold"))
   dollar_box.pack(pady=10)
   tk.Label(win, text="Dollar", font=("Arial", 12, "bold")).pack(pady=10)



   dollar_label = tk.Label(win, font=("Arial", 12, "bold"))
   dollar_label.pack(pady=10)

   peso_label = tk.Label(win, font=("Arial", 12, "bold"))
   peso_label.pack(pady=10)

   def show_currency():
       try:
           if peso_box.get() != "":
               peso = float(peso_box.get())
               dollar = peso / 50
               dollar_label.config(text="In Dollar " + str(round(dollar, 2)))


           elif dollar_box.get() != "":
               dollar = float(dollar_box.get())
               peso = dollar * 50
               peso_label.config(text="In Peso " + str(round(peso, 2)))

       except ValueError:
           peso_label.config(text="Invalid Input")
           dollar_label.config(text="Invalid Input")

   submit_button = tk.Button(win, text="Submit", command=show_currency)
   submit_button.pack(pady=10)