# write a program to play rock paper scissor with computer
"""
1. take user input
2. let computer pick either rock paper or scissor
3. print user/computer wins!

Priority
    - rock > scissor
    - scissor > paper
    - paper > rock
"""
import random


def play_with_computer():
    """rock > scissor; scissor > paper;   paper > rock"""
    user_input = input("Enter rock, paper or scissor:").strip().lower()
    if user_input not in ("rock", "paper", "scissor"):
        return "INVALID INPUT"
    computer_input = random.choice(["rock", "paper", "scissor"])
    print(f"computer_input = {computer_input}")
    if user_input == computer_input:
        return "draw"

    if (
        (user_input == "rock" and computer_input == "scissor")
        or (user_input == "scissor" and computer_input == "paper")
        or (user_input == "paper" and computer_input == "rock")
    ):
        return "USER WINS"
    return "COMPUTER WINS"


def play_with_computer():
    """rock > scissor; scissor > paper;   paper > rock"""
    user_input = input("Enter rock, paper or scissor:").strip().lower()
    if user_input not in ("rock", "paper", "scissor"):
        return "INVALID INPUT"
    computer_input = random.choice(["rock", "paper", "scissor"])
    print(f"computer_input = {computer_input}")
    if user_input == computer_input:
        return "draw"
    relation = {"rock": "scissor", "scissor": "paper", "paper": "rock"}
    if computer_input == relation[user_input]:
        return "USER WINS"
    return "COMPUTER WINS"


if __name__ == "__main__":
    print(play_with_computer())
