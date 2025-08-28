#Basic Dice Game

import random
import tkinter as tk

rolling_count = 0
player_score = 0
computer_score = 0

def roll_dice():
       global rolling_count, player_score, computer_score
       if rolling_count > 0:
        computer = random.randint(1, 6)
        player = random.randint(1, 6)
        player_label.config(text="You rolled: " + str(player))
        computer_label.config(text="Computer rolled: " + str(computer))
        rolling_count -= 1
        root.after(150, roll_dice)

       else:
         final_player = random.randint(1, 6)
         final_computer = random.randint(1, 6)
         player_label.config(text="You Rolled: "+str(final_player))
         computer_label.config(text="Computer Rolled: "+str(final_computer))


         if final_player > final_computer:
            result_label.config(text="✅You Win the Round!", fg="green")
            update_score("player")



         elif final_player < final_computer:
             result_label.config(text="❌Computer Wins the Round!", fg="red" )
             update_score("computer")
         else:
             result_label.config(text="🤝It's a tie!", fg="orange")

def start_game():
        global rolling_count
        result_label.config(text="")
        rolling_count = 10
        roll_dice()

def update_score(winner):
        global player_score, computer_score
        if winner == "computer":
           computer_score += 1
        elif winner == "player":
            player_score += 1

        score_label.config(text=f"Score: Player  {player_score} - {computer_score} Computer")


        if computer_score == 3:
            computer_label.config(text="Computer Champion! 🏆")
            player_label.config(text="You Lose!")
            disable_button()



        elif player_score == 3:
            player_label.config(text="You Champion! 🏆")
            computer_label.config(text="Computer Lose!")
            disable_button()



def disable_button():
     roll_button.config(state="disabled")

def reset_game():
        global player_score, computer_score
        player_score = 0
        computer_score = 0


        score_label.config(text="Score: Player 0 - 0 Computer")
        result_label.config(text="")
        roll_button.config(state="normal")



root = tk.Tk()
root.title("Best of Five Dice Game")
root.geometry("300x200")

roll_button = tk.Button(root, text="Roll 🎲", fg="white", bg="black",command=start_game)
roll_button.pack(pady=10)

reset_button = tk.Button(root, text="Reset Game", fg="white", bg="blue",command=reset_game)
reset_button.pack(pady=10)

computer_label=tk.Label(root, text="Computer rolled: -", fg="white", bg="black")
computer_label.pack()

player_label=tk.Label(root, text="Player rolled: -", fg="white", bg="black")
player_label.pack()

score_label=tk.Label(root, text="Score: Player 0 - 0 Computer", font=("Arial", 12, "bold"))
score_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

root.mainloop()
