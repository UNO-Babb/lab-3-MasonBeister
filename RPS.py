#RPS.py
#Name:
#Date:
#Assignment:
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.
  play = "Y"
  while play == "Y":

    player = input("Enter choice (R), (P), (S): ")

    computer = random.choice(["R", "P", "S"])

    if player == "R":
      print("Player chose Rock")
    elif player == "P":
      print("Player chose Paper")
    elif player == "S":
      print("Player chose Scissors")
    else:
      print("Invalid Option")

    if player == computer: 
      print("TIE")
      ties = ties + 1
    elif player == "R" and computer == "S":
      print("You Win!")
      wins = wins + 1
    elif player == "R" and computer == "P":
      print("You Lose.")
      losses = losses + 1
    elif player == "P" and computer == "R":
      print("You Win!")
      wins = wins + 1
    elif player == "P" and computer == "S":
      print("You Lose.")
      losses = losses + 1
    elif player == "S" and computer == ("P"):
      print("You Win!")
      wins = wins + 1
    elif player == "S" and computer == ("R"):
      print("You Lose.")
      losses = losses + 1

 
 
    play = input("Play again? (Y/N): ")
  play = "N"
  print("End of game")


  #Randomly choose the computer between 'R', 'P', or 'S'
  #Prompt the user for their RPS selection
  #Determine winner and state what happened to the user
  #Ask the user if they would like to play again.

  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
