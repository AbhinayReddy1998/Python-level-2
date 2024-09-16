import random

options=("rock","paper","scissors")
running=True
print("Welcome to RPS Game")

while running:

    computer=random.choice(options)
    player=None

    while player not in options:
        player= input("Enter a choice (rock , paper , scissors):  ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")
    if player==computer:
        print("Its a tie!")
    elif player=="rock" and computer =="scissors":
     print("Hey congrats! You won")
    elif player=="paper" and computer == "rock":
     print("Hey congrats! You won")
    elif player=="scissors" and computer == "paper":
     print("Hey congrats! You won")
    else:
     print("Sorry,You lost!") 
    play_again=input("Play again? (y/n): ").lower()
    if not play_again =="y":
     running= False
    print("Thanks for playing!")
    