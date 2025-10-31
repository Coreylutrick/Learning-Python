import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

print("")

player_choice = input("Enter...\n1 for Rock\n2 for Paper\n3 for Scissor\n\n")

player = int(player_choice)

if player < 1 | player > 3:
    sys.exit("Pick a number 1 through 3")

computer_choice = random.choice("123")

computer = int(computer_choice)

print("")
print("You chose " + str(RPS(player)).replace("RPS.", "") + ".")
print("Python chose " + str(RPS(computer)).replace("RPS.", "") + ".")
print("")

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
