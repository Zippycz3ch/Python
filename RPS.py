player_1 = input("Rock, Paper or Scissors?")
print(" No cheating\n" *20)
player_2 = input("Rock, Paper or Scissors?")

if player_1 == "Rock" and player_2 == "Scissors" or player_1 == "Scissors" and player_2 == "Paper" or player_1 == "Paper" and player_2 == "Rock":
    print("Player 1 wins")
elif player_2 == "Rock" and player_1 == "Scissors" or player_2 == "Scissors" and player_1 == "Paper" or player_2 == "Paper" and player_1 == "Rock":
    print("Player 1 wins")
else:
    print("Play Again!") 