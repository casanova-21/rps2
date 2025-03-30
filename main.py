import tkinter as tk
from tkinter import messagebox
import random
import itertools

# Initialize score counters
user_score = 0
computer_score = 0

def update_score(result):
    global user_score, computer_score
    if result == "You win!":
        user_score += 1
    elif result == "You lose!":
        computer_score += 1
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

# Refactor game logic into a separate function
def get_game_result(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

# New function to handle game logic and return results and scores
def process_game(user_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    result = get_game_result(user_choice, computer_choice)

    global user_score, computer_score
    if result == "You win!":
        user_score += 1
    elif result == "You lose!":
        computer_score += 1

    return computer_choice, result, user_score, computer_score

# Update play_game to use the new function
def play_game(user_choice):
    computer_choice, result, user_score, computer_score = process_game(user_choice)
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

def quit_game():
    root.destroy()

def blink_button_text(button, colors):
    color_cycle = itertools.cycle(colors)

    def update_color():
        button.config(fg=next(color_cycle))
        button.after(500, update_color)

    update_color()

def center_window(window):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    size = tuple(int(_) for _ in window.geometry().split('+')[0].split('x'))
    x = screen_width // 2 - size[0] // 2
    y = screen_height // 2 - size[1] // 2
    window.geometry(f"{size[0]}x{size[1]}+{x}+{y}")

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Update the main window background color
root.configure(bg="lightblue")

# Create widgets
welcome_label = tk.Label(root, text="Welcome to Rock, Paper, Scissors!", font=("Arial", 16))
welcome_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: play_game("rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: play_game("paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play_game("scissors"))
scissors_button.grid(row=0, column=2, padx=5)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

quit_button = tk.Button(root, text="Quit", command=quit_game)
quit_button.pack(pady=10)

# Add a score label
score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Arial", 14), bg="lightblue", fg="darkred")
score_label.pack(pady=10)

# Update widget styles
welcome_label.config(bg="lightblue", fg="darkblue")
result_label.config(bg="lightblue", fg="darkgreen")

# Update button styles and add blinking text
button_colors = ["red", "blue", "green"]
rock_button.config(bg="white", activebackground="lightgray")
paper_button.config(bg="white", activebackground="lightgray")
scissors_button.config(bg="white", activebackground="lightgray")
quit_button.config(bg="white", activebackground="lightgray")

blink_button_text(rock_button, button_colors)
blink_button_text(paper_button, button_colors)
blink_button_text(scissors_button, button_colors)
blink_button_text(quit_button, button_colors)

# Adjust the window size to fit all content
root.geometry("500x400")

# Center the main window
center_window(root)

# Run the application
root.mainloop()