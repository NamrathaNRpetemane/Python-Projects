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

game_images = [rock, paper, scissors]

user_choice = int(input("what do you choose? Type 0 for Rock, Type 1 for Paper, Type 2 for Scissor."))

if user_choice >= 0 or user_choice <= 2:
    print(game_images[user_choice])


print("Computer Choice")
computer_choice = random.randint(0, 2)
print(game_images[computer_choice])


if user_choice == 0 and computer_choice == 2:
    print("You Win...!")
elif computer_choice == 0 and user_choice == 2:
    print("You Loose...!")
elif computer_choice > user_choice:
    print("You Loose...!")
elif user_choice > computer_choice:
    print("You Win...!")
else:
    print("It's a draw!")




# implement in better way using try and catch

import random

# Define the choices and game logic
game_images = ["Rock", "Paper", "Scissors"]
game_rules = {
    0: 2,  # Rock beats Scissors
    1: 0,  # Paper beats Rock
    2: 1   # Scissors beats Paper
}

# User input
try:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
    if user_choice not in [0, 1, 2]:
        raise ValueError("Invalid choice, must be 0, 1, or 2.")
except ValueError as e:
    print(f"Error: {e}")
    exit()

# Show user choice
print(f"You chose: {game_images[user_choice]}")

# Computer choice
computer_choice = random.randint(0, 2)
print(f"Computer chose: {game_images[computer_choice]}")
print(game_rules[user_choice])

# Determine the winner
if user_choice == computer_choice:
    print("It's a draw!")
elif game_rules[user_choice] == computer_choice:
    print("You Win!")
    
else:
    print("You Lose!")


print(game_rules[0])
print(game_rules[1])
print(game_rules[2])




    

