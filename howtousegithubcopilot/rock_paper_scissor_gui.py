"""
Rock Paper Scissors GUI Game using Tkinter
A graphical interface version of the Rock Paper Scissors game
"""

import tkinter as tk
from tkinter import font
import random


class RockPaperScissorsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")
        self.root.geometry("500x600")
        self.root.configure(bg="#f0f0f0")

        # Game variables
        self.player_score = 0
        self.computer_score = 0
        self.choices = ["rock", "paper", "scissors"]

        # Title
        title_font = font.Font(family="Helvetica", size=24, weight="bold")
        title_label = tk.Label(self.root, text="Rock Paper Scissors", font=title_font, bg="#f0f0f0")
        title_label.pack(pady=20)

        # Score display
        self.score_font = font.Font(family="Helvetica", size=14, weight="bold")
        self.score_label = tk.Label(
            self.root,
            text=f"Player: {self.player_score}  |  Computer: {self.computer_score}",
            font=self.score_font,
            bg="#f0f0f0",
        )
        self.score_label.pack(pady=10)

        # Game result display
        self.result_font = font.Font(family="Helvetica", size=16, weight="bold")
        self.result_label = tk.Label(
            self.root, text="Make your move!", font=self.result_font, bg="#f0f0f0", fg="#333333"
        )
        self.result_label.pack(pady=20)

        # Computer choice display
        self.choice_font = font.Font(family="Helvetica", size=12)
        self.choice_label = tk.Label(self.root, text="Computer's choice: ---", font=self.choice_font, bg="#f0f0f0")
        self.choice_label.pack(pady=10)

        # Button frame
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=30)

        # Button styling
        button_font = font.Font(family="Helvetica", size=12, weight="bold")
        button_width = 12
        button_height = 3

        # Rock button
        rock_button = tk.Button(
            button_frame,
            text="🪨 Rock",
            font=button_font,
            width=button_width,
            height=button_height,
            command=lambda: self.play_game("rock"),
            bg="#e74c3c",
            fg="white",
            activebackground="#c0392b",
        )
        rock_button.grid(row=0, column=0, padx=10)

        # Paper button
        paper_button = tk.Button(
            button_frame,
            text="📄 Paper",
            font=button_font,
            width=button_width,
            height=button_height,
            command=lambda: self.play_game("paper"),
            bg="#3498db",
            fg="white",
            activebackground="#2980b9",
        )
        paper_button.grid(row=0, column=1, padx=10)

        # Scissors button
        scissors_button = tk.Button(
            button_frame,
            text="✂️ Scissors",
            font=button_font,
            width=button_width,
            height=button_height,
            command=lambda: self.play_game("scissors"),
            bg="#2ecc71",
            fg="white",
            activebackground="#27ae60",
        )
        scissors_button.grid(row=0, column=2, padx=10)

        # Reset button
        reset_button = tk.Button(
            self.root,
            text="Reset Score",
            font=button_font,
            command=self.reset_score,
            bg="#95a5a6",
            fg="white",
            activebackground="#7f8c8d",
            padx=20,
            pady=10,
        )
        reset_button.pack(pady=20)

    def get_computer_choice(self):
        """Get a random choice for the computer"""
        return random.choice(self.choices)

    def determine_winner(self, player_choice, computer_choice):
        """Determine the winner of the round"""
        if player_choice == computer_choice:
            return "tie"
        elif (
            (player_choice == "rock" and computer_choice == "scissors")
            or (player_choice == "paper" and computer_choice == "rock")
            or (player_choice == "scissors" and computer_choice == "paper")
        ):
            return "player"
        else:
            return "computer"

    def play_game(self, player_choice):
        """Execute one round of the game"""
        computer_choice = self.get_computer_choice()
        result = self.determine_winner(player_choice, computer_choice)

        # Update scores
        if result == "player":
            self.player_score += 1
            result_text = "🎉 You Win!"
            result_color = "#2ecc71"
        elif result == "computer":
            self.computer_score += 1
            result_text = "🤖 Computer Wins!"
            result_color = "#e74c3c"
        else:
            result_text = "🤝 It's a Tie!"
            result_color = "#f39c12"

        # Update display labels
        self.result_label.config(text=result_text, fg=result_color)
        self.choice_label.config(text=f"Computer chose: {computer_choice.capitalize()}")
        self.score_label.config(text=f"Player: {self.player_score}  |  Computer: {self.computer_score}")

    def reset_score(self):
        """Reset the game scores"""
        self.player_score = 0
        self.computer_score = 0
        self.score_label.config(text=f"Player: {self.player_score}  |  Computer: {self.computer_score}")
        self.result_label.config(text="Make your move!", fg="#333333")
        self.choice_label.config(text="Computer's choice: ---")


if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGUI(root)
    root.mainloop()
