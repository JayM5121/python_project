"""
WORKFLOW OF PROJECTS

1 - Inputs from users = (Rock, Paper, Scissor)
2 - Computer choice (Computer will choose randomly not conditionally
3 - Print Result

Cases :
    A = Rock
    Rock - Rock = Tie
    Rock - Paper = Paper Win
    Rock - Scissor = Rock Win

    B = Paper
    Paper - Paper = Tie
    Paper - Rock = Rock Win
    Paper - Scissor = Scissor Win

    C = Scissor
    Scissor - Scissor = Tie
    Scissor - Rock = Rock Win
    Scissor - Paper = Scissor Win
"""

import random
item_list = ["rock", "paper", "scissor"]

user_choice = input("Enter your move : (rock, paper, scissor) = ").strip().lower()
computer_choice = random.choice(item_list)

print(f"User Choice {user_choice.capitalize()}, Computer Choice {computer_choice.capitalize()}")

if user_choice.lower() == computer_choice.lower():
    print("Both choose same :- Match Tie")

elif user_choice == "rock":
    if computer_choice == "Paper":
        print("Paper cover rock :- Computer win")
    else:
        print("Rock smashes scissor :- You Will")

elif user_choice == "paper":
    if computer_choice == "Scissor":
        print("Scissor cuts paper :- Computer Win")
    else:
        print("Paper cover rock :- You Win")

elif user_choice == "scissor":
    if computer_choice == "Paper":
        print("Scissor cuts paper :- You Win")
    else:
        print("Rock smashes paper :- Computer win")
else:
    print("Invalid input! Please choose Rock, Paper, or Scissor.")