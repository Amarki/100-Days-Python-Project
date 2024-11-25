# Day 4 - Rock, Paper, Scissors
#Purpose: Practicing random variable inputs and the use of lists in combination to create a program that simulates a game of Rock paper scissors.

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

handsign = [rock, paper, scissors]
decision = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
opponent = random.randint(0,2)

print(f"You chose: {handsign[decision]}")
print(f"They chose: {handsign[opponent]}")


if decision >= 3 and decision < 0:
    print("That isn't a hand sign for the game! You explode and lose! *BOOM!*")
elif decision == opponent:
    print("You both draw!")
elif decision == 0 and opponent == 2:
    print("You win!")
elif opponent == 0 and decision == 2:
    print("You lose!")
elif decision > opponent:
    print("You win!")
elif opponent > decision:
    print("You lose!")
