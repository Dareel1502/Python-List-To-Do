#Basic Password Generator

import getpass
import string
import tkinter as tk
import random
pass_generator = string.ascii_letters + string.digits + string.punctuation
random_pass = ''.join(random.choice(pass_generator) for _ in range(12))

def show_credits():
    global random_pass, uname
    result_pass.config(text='Password: ' + random_pass)

    uname = text_box.get("1.0", tk.END)
    result_uname.config(text="Enter Your Username:  " + uname)

root = tk.Tk()
root.title("Password Generator")
root.geometry("300x300")

uname = tk.Label(root, text="Enter your username", font=("Arial", 12, "bold"))
uname.pack(pady=10)

text_box = tk.Text(root, width=20, height=3, font=("Arial", 12, "bold"))
text_box.pack(pady=10)

show_button = tk.Button(root, text="Generate Account", command=show_credits)
show_button.pack(padx=5, pady=5)

result_uname = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_uname.pack(pady=10)

result_pass = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_pass.pack(pady=10)


root.mainloop()