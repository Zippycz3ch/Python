import random
player_1 = input("Rock, Paper or Scissors?")
player_2 = random.randint(1,3)
if player_2 == 1:
    player_2 = "Rock"
    print("PC plays rock")
elif player_2 == 2:
    player_2 = "Scissors"
    print("PC plays Scissors")
else:
    player_2 = "Paper"
    print("PC plays Paper")
    

if player_1 == "Rock" and player_2 == "Scissors" or player_1 == "Scissors" and player_2 == "Paper" or player_1 == "Paper" and player_2 == "Rock":
    print("Player 1 wins")
elif player_2 == "Rock" and player_1 == "Scissors" or player_2 == "Scissors" and player_1 == "Paper" or player_2 == "Paper" and player_1 == "Rock":
    print("Player 1 wins")
else:
    print("Play Again!") 