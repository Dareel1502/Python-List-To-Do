import tkinter as tk

def show_result():
      try:
         num1 =float(entry1.get())
         num2 =float(entry2.get())
         operator = entry3.get()

         if operator == "+":
           result = num1 + num2
         elif operator == "-":
          result = num1 - num2
         elif operator == "*":
          result = num1 * num2
         elif operator == "/":

                if num2 == 0:
                   result_label.config(text="You can't divide by zero")
                   return
                else:
                   result = num1 / num2
         else:
                result = "Please enter valid Operator!"
         result_label.config(text=str(result))
      except ValueError:
         result_label.config(text="Please enter valid Number!")

root = tk.Tk()
root.title("Sample Calculator")

tk.Label(root, text="Enter a 1st number: ",fg="white", bg="black").pack()
entry1 = tk.Entry(root, font=("Arial", 20), fg="white", bg="black")
entry1.pack(pady=10)

tk.Label(root, text="Enter Operator( +, - , *, / :  )", fg="white", bg="black").pack()
entry3 = tk.Entry(root, font=("Arial", 20), fg="white", bg="black")
entry3.pack(pady=10)

tk.Label(root, text="Enter a 2nd number: ",fg="white", bg="black").pack()
entry2 = tk.Entry(root, font=("Arial", 20), fg="white", bg="black")
entry2.pack(pady=10)

tk.Button(root, text="Submit", fg="white", bg="black",command=show_result).pack(pady=10)


result_label = tk.Label(root, text="", fg="white", bg="black")
result_label.pack()

root.mainloop()




