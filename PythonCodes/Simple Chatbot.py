import tkinter as tk

# Function to handle sending messages
def send_message():
    user_input = entry.get().lower()
    chat_window.insert(tk.END, "You: " + user_input + "\n")
    entry.delete(0, tk.END)


    responses = {
        "hi": "Hello there! How can I help you?",
        "hello": "Hi! Nice to meet you.",
        "how are you": "I'm just a bot, but I'm doing great! Thanks for asking.",
        "what is your name": "I'm ChatBot 1.0, your virtual assistant.",
        "bye": "Goodbye! Have a great day!",
        "who created you?": "I created by Daryl Hans Ocao",
        "what is your purpose?": "My purpose is to assist people by providing information, answering questions, and making tasks easier through AI."

    }


    if user_input in responses:
        reply = responses[user_input]
        chat_window.insert(tk.END, "Bot: " + reply + "\n")
        if user_input == "bye":
            root.quit()
    else:
        chat_window.insert(tk.END, "Bot: Sorry, I don't understand that.\n")



root = tk.Tk()
root.title("Simple Chatbot")


chat_window = tk.Text(root, height=20, width=50)
chat_window.pack(padx=10, pady=10)


entry = tk.Entry(root, width=40)
entry.pack(side=tk.LEFT, padx=10, pady=10)


send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.LEFT)

root.mainloop()
