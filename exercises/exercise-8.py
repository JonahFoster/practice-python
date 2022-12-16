# Make a two-player Rock-Paper-Scissors game. 
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

player1 = input("Player 1 input Rock, Paper, or Scissors: ")
player2 = input("Player 2 input Rock, Paper, or Scissors: ")

while (player1 == player2):
    print("A tie! Play again.")
    player1 = input("Player 1 input Rock, Paper, or Scissors: ")
    player2 = input("Player 2 input Rock, Paper, or Scissors: ")

while (player1 != player2):
    if player1 == "rock" and player2 == "scissors":
        print("Player 1 Wins!")
        break
    elif player1 == "rock" and player2 == "paper":
        print("Player 2 wins!")
        break
    elif player1 == "paper" and player2 == "rock":
        print("Player 1 wins!")
        break
    elif player1 == "paper" and player2 == "scissors":
        print("Player 2 wins!")
        break
    elif player1 == "scissors" and player2 == "paper":
        print("Player 1 wins!")
        break
    elif player1 == "scissors" and player2 == "rock":
        print("Player 2 wins!")
        break