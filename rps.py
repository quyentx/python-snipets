import random

options = ["rock", "paper", "scissors"]
player1 = random.choice(options)
print("The computer made its choice. It's your turn!")
player2 = input("Your choice: ")
if player2 in options:
    if player1 == player2:
        print("Draw")
    elif player1 == "rock" and player2 == "scissors":
        print("Computer plays " + player1 + ". Computer wins!")
    elif player1 == "paper" and player2 == "rock":
        print("Computer plays " + player1 + ". Computer wins!")
    elif player1 == "scissors" and player2 == "paper":
        print("Computer plays " + player1 + ". Computer wins!")
    else:
        print("Computer plays " + player1 + ". You wins!")
else:
    print("***No cheating***")
