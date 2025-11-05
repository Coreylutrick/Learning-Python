import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

playagain = True

while playagain:

    player_choice = input("\nEnter...\n1 For Rock\n2 For Paper\n3 For Scissor\n\n")

    player = int(player_choice)

    if player < 1 or player > 3:
        sys.exit("Pick a number 1 through 3")

    computer_choice = random.choice("123")

    computer = int(computer_choice)

    print("\nYou chose " + str(RPS(player)).replace("RPS.", "") + ".")
    print("Python chose " + str(RPS(computer)).replace("RPS.", "") + ".\n")


    if player == 1 and computer == 3:
        print("You win 😊!")
    elif player == 2 and computer == 1:
        print("You win 😊!")
    elif player == 3 and computer == 2:
        print("You win 😊!")
    elif player == computer:
        print("It's a tie!")
    else:
        print("Python wins 🐍)")

    playagain = input("\n Play again?\nY for yes or \nN for no \n\n")

    if playagain.lower() == "y":
        continue
    else:
        print("\n👌")
        print("Thank you for playing.")
        playagain = False

sys.exit("Bye!")
