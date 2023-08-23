# This is a simple rock-paper-scissor game. The game was actually supposed to take the input as 0,1 or 2, but I wanted a challenge... Soooooo it was as 'rock', 'paper' and 'scissor'.
# Day Goal: Learn more about randomization and python lists

import random

choice_art = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""", """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""", """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]

print("Welcome to my rock-paper-scissor game".center(50,'-'))
print()

game_choices = ["rock","paper","scissor"]
users_choice = input("What do you choose? Rock, Paper or Scissors: ").lower()

if users_choice in game_choices:
    computers_choice = random.choice(game_choices)

    print(f"You chose: {users_choice}\n{choice_art[game_choices.index(users_choice)]}")

    print(f"Computer chose: {computers_choice}\n{choice_art[game_choices.index(computers_choice)]}")

    if users_choice == computers_choice:
        print("\nThe game is a draw!")
    elif users_choice == "rock" and computers_choice == "scissor":
        print("\nYou won!")
    elif computers_choice == "rock" and users_choice == "scissor":
        print("\nYou lose!")
    elif game_choices.index(users_choice) < game_choices.index(computers_choice):
        print("\nYou lose!")
    elif game_choices.index(users_choice) > game_choices.index(computers_choice):
        print("\nYou won!")
    else:
        print("|nInvalid input. You lose!")

else: 
    print("\nYou entered an invalid choice.\nGame Over!")
