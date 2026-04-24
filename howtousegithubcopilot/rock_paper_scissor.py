"""
Create a Rock Paper Scissors game where the player inputs their choice and plays against a
computer that randomly selects its move, with the game showing who won each round.
Add a score counter that tracks player and computer wins, and allow the game to continue
until the player types 'quit'
"""

import random


def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "paper" and computer_choice == "rock")
        or (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "Player wins!"
    else:
        return "Computer wins!"


def main():
    player_score = 0
    computer_score = 0

    while True:
        raw_input_choice = input("Enter rock (r), paper (p), scissors (s) or 'quit' to exit: ").strip().lower()
        # allow shortcuts r/p/s
        if raw_input_choice in ("r", "p", "s"):
            player_choice = {"r": "rock", "p": "paper", "s": "scissors"}[raw_input_choice]
        else:
            player_choice = raw_input_choice

        if player_choice == "quit":
            print("Thanks for playing!")
            break

        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(result)

        if result == "Player wins!":
            player_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"Score - Player: {player_score}, Computer: {computer_score}\n")


if __name__ == "__main__":
    main()
